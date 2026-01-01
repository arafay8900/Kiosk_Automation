# conftest.py
import os
import base64
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_html import extras

# -------------------------
# Pytest Fixture: WebDriver
# -------------------------
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# -------------------------
# Step Logs Storage
# -------------------------
step_logs = {}

# -------------------------
# Pytest Fixture: Logger
# -------------------------
@pytest.fixture
def logger(request, driver):
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

        # Add log entry
        step_logs[test_name].append({
            "message": message,
            "screenshot_base64": img_base64
        })

    return log

# -------------------------
# Pytest Hook: Attach Logs & Screenshots to HTML Report
# -------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        test_name = item.name
        extras_list = getattr(rep, "extras", [])  # <-- updated to 'extras'

        for step in step_logs.get(test_name, []):
            extras_list.append(extras.text(step["message"]))
            extras_list.append(extras.image(step["screenshot_base64"]))

        rep.extras = extras_list  # <-- updated to 'extras'
