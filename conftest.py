# conftest.py
import os
import base64
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pytest_html import extras
import allure
import cv2
import mss
import numpy as np
import threading
import time
import logging

# Suppress urllib3 warnings
logging.getLogger("urllib3").setLevel(logging.ERROR)

# ------------------------- 
# Pytest Fixture: Browser Parameter
# -------------------------
@pytest.fixture(params=["chrome", "firefox", "edge"])
def browser(request):
    """Fixture to parameterize tests across different browsers."""
    return request.param

# -------------------------
# Pytest Fixture: WebDriver
# -------------------------
@pytest.fixture
def driver(browser):
    """Fixture to create WebDriver instance based on browser parameter."""
    # Selenium Manager (built into Selenium 4.6+) resolves and downloads the
    # driver matching whatever browser version is installed, no separate
    # webdriver-manager dependency or pinned driver binaries to go stale.
    #
    # --no-sandbox/--disable-dev-shm-usage: Chromium crashes on launch in CI
    # containers without them (restricted namespaces, tiny /dev/shm).
    # --start-maximized instead of a post-launch maximize_window() call:
    # maximize_window() depends on real window-manager behavior that a bare
    # Xvfb display doesn't reliably provide.
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)

    # Fail fast on a hung renderer instead of blocking for minutes: without
    # these, a stuck page load or execute_script() call can hang well past
    # any of HomePage's own WebDriverWait timeouts.
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)

    yield driver
    driver.quit()

# ------------------------- 
# Screen Recorder Class
# -------------------------
class ScreenRecorder:
    """Class to record screen during test execution."""

    def __init__(self, driver):
        """Initialize the recorder with the WebDriver instance."""
        self.driver = driver
        self.frames = []
        self.recording = False
        self.thread = None

    def start(self):
        """Start recording in a separate thread."""
        self.recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()

    def _record(self):
        """Internal method to capture frames from the browser window."""
        with mss.mss() as sct:
            pos = self.driver.get_window_position()
            size = self.driver.get_window_size()
            bbox = {'left': pos['x'], 'top': pos['y'], 'width': size['width'], 'height': size['height']}
            while self.recording:
                img = sct.grab(bbox)
                frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)
                self.frames.append(frame)
                time.sleep(0.2)  # 5 fps

    def stop(self):
        """Stop recording and return captured frames."""
        self.recording = False
        if self.thread:
            self.thread.join()
        return self.frames

# ------------------------- 
# Pytest Fixture: Screen Recorder
# -------------------------
@pytest.fixture
def screen_recorder(request, driver):
    """Fixture to record screen during test and attach video to Allure."""
    recorder = ScreenRecorder(driver)
    recorder.start()
    yield recorder
    frames = recorder.stop()
    if frames:
        height, width, _ = frames[0].shape
        video_path = f"reports/videos/{request.node.name}.mp4"
        os.makedirs(os.path.dirname(video_path), exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_path, fourcc, 5.0, (width, height))
        for frame in frames:
            out.write(frame)
        out.release()
        allure.attach.file(video_path, name="Test Video", attachment_type=allure.attachment_type.MP4)

# -------------------------
# Step Logs Storage
# -------------------------
step_logs = {}

# -------------------------
# Pytest Fixture: Logger
# -------------------------
@pytest.fixture
def logger(request, driver):
    """Fixture to log steps with screenshots for HTML and Allure reports."""
    test_name = request.node.name
    if test_name not in step_logs:
        step_logs[test_name] = []

    def log(message):
        # Create screenshots directory if it doesn't exist
        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        # Save screenshot
        screenshot_path = f"{screenshots_dir}/{test_name}_{len(step_logs[test_name])+1}.png"
        driver.save_screenshot(screenshot_path)

        # Convert screenshot to base64
        with open(screenshot_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode("utf-8")

        # Attach to Allure
        allure.attach.file(screenshot_path, name=f"Step {len(step_logs[test_name])+1}: {message}", attachment_type=allure.attachment_type.PNG)

        # Add log entry
        step_logs[test_name].append({
            "message": message,
            "screenshot_base64": img_base64
        })

    return log

    return log

# -------------------------
# Pytest Hook: Attach Logs, Screenshots, and Video Links to Reports
# -------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        test_name = item.name
        extras_list = getattr(rep, "extras", [])

        # Attach step logs and screenshots to HTML report
        for step in step_logs.get(test_name, []):
            extras_list.append(extras.text(step["message"]))
            extras_list.append(extras.image(step["screenshot_base64"]))

        # Add video link to HTML report
        video_path = f"videos/{test_name}.mp4"
        if os.path.exists(f"reports/{video_path}"):
            extras_list.append(extras.html(f'<a href="{video_path}" target="_blank">Download Test Video</a>'))

        rep.extras = extras_list

        # Attach screenshot on failure to Allure. A diagnostics step must
        # never be able to crash the run it's diagnosing, if the browser is
        # already dead/unresponsive (the likely reason the test just
        # failed), skip the screenshot instead of raising a second
        # exception inside pytest's own reporting hook.
        if rep.failed:
            driver = item.funcargs.get('driver')
            if driver:
                try:
                    allure.attach(driver.get_screenshot_as_png(), name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)
                except Exception as e:
                    print(f"Could not capture failure screenshot: {e}")
