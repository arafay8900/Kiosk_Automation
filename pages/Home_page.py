import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """Page object for the Kiosk Home Page, handling visitor check-in flow."""

    LOADER = (By.CLASS_NAME, "loader")

    CHECK_IN_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]/div/button[3]")
    CHOSE_WORKFLOW = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]")
    NEXT_MULTIPARTY = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div/button[2]")
    PHONE_INPUT = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/div/div[2]/input")
    PHONE_Next = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/button[2]")
    CHOSE_PROFILE = (
        By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[2]")
    CHOSE_HOST = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[9]")
    UPLOAD_BUTTON = "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/button"
    UPLOAD_FILE_PATH = r"C:\Users\AbdulRafay\Downloads\1380678.jpg"
    UPLOAD_NEXT = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/button")
    DOX_NEXT_BUTTON = (
        By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div/button")
    PPTX_NEXT2_BUTTON = (
        By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div/div/button")
    TEST_OPTION_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div[1]")
    TEST_OPTION_WITHOUT_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/button")
    CLOSE_IMAGE_BUTTON = (
        By.XPATH, "/html/body/div[3]/div[4]")
    TEST_SUBMIT_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/button")
    CONTENT_NEXT_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/button")
    VISIT_LINK_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/button")

    def __init__(self, driver, logger=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100, poll_frequency=3)
        self.logger = logger

    def _log(self, message):
        if self.logger:
            self.logger(message)

    def _click(self, locator, message):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self._log(message)

    def wait_for_api(self, timeout=100):
        """Wait for page to load and API calls to complete."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located(self.LOADER)
                )
            except TimeoutException:
                pass  # Loader not present, ignore
            self._log("API completed successfully")
        except TimeoutException:
            self._log("API timeout exceeded")
            raise

    def open(self):
        self.driver.get("https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/home")
        self._log("Opened home page")

    def home_url(self):
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/home"

    def click_check_in(self):
        self._click(self.CHECK_IN_BUTTON, "Clicked Check In button")

    def visitor_type_url(self):
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/visitor-type"

    def click_chose_workflow(self):
        self._click(self.CHOSE_WORKFLOW, "Chose workflow clicked")

    def num_people_url(self):
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/num-people"

    def click_next_multiparty(self):
        self._click(self.NEXT_MULTIPARTY, "Next button clicked")

    def visitor_info_url(self):
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/visitor-info"

    def phone_input(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_INPUT)).send_keys("3021843163")
        self._log("Phone number entered")

    def click_phone_next(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_Next)).click()
        self.wait_for_api()
        self._log("Phone Next button clicked")

    def chose_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_PROFILE)).click()
        self.wait_for_api()
        self._log("Clicked on Profile")

    def chose_host_url(self):
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/choose-host"

    def click_chose_host(self):
        self._click(self.CHOSE_HOST, "Clicked on Search Host icon")

    def upload_file(self, upload_xpath: str = None, file_path: str = None, timeout: int = 30):
        """Upload a file using the provided xpath/button.

        Behavior:
        - First, try to find an `input[type=file]` anywhere on the page and send the file path directly (avoids opening native dialog).
        - If no input found, click the provided element to potentially reveal it, then find and send.
        - If the provided xpath is directly an input[type=file], send directly.

        Note: Selenium cannot interact with native OS file dialogs. Sending
        a path to an `input[type=file]` avoids opening the OS dialog.
        """
        upload_xpath = upload_xpath or getattr(self, 'UPLOAD_BUTTON', None)
        file_path = file_path or getattr(self, 'UPLOAD_FILE_PATH', None)
        if not upload_xpath or not file_path:
            raise ValueError('upload_xpath and file_path must be provided either as args or set on the page object')

        locator = (By.XPATH, upload_xpath)
        el = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

        try:
            is_file_input = el.tag_name.lower() == 'input' and (el.get_attribute('type') or '').lower() == 'file'
        except Exception:
            is_file_input = False

        if is_file_input:
            return self._finish_upload(el, file_path, "direct input")

        # Try an input[type=file] already present on the page without clicking
        try:
            file_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            return self._finish_upload(file_input, file_path, "existing input")
        except Exception:
            pass

        # Click the provided element to reveal a hidden file input
        try:
            el.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", el)

        try:
            file_input = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            return self._finish_upload(file_input, file_path, "discovered input")
        except Exception:
            pass

        # Last resort: an input nested under the clicked element
        try:
            nested = el.find_element(By.XPATH, ".//input[@type='file']")
            return self._finish_upload(nested, file_path, "nested input")
        except Exception:
            pass

        raise Exception(
            "Could not find an input[type=file] to upload the file. "
            "If your UI uses a native file dialog, locate a hidden file input and pass its xpath."
        )

    def _finish_upload(self, file_input, file_path, source):
        file_input.send_keys(file_path)
        self.wait_for_api()
        self._log(f"Uploaded file via {source}: {file_path}")

    def close_new_tab(self, wait_seconds: int = 4):
        """If clicking a link opened a new browser tab/window, keep it open briefly then close it and return focus to the main window."""
        main_handle = self.driver.current_window_handle
        try:
            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        except TimeoutException:
            self._log("No new window/tab appeared")
            return

        time.sleep(wait_seconds)

        for handle in self.driver.window_handles:
            if handle != main_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()

        self.driver.switch_to.window(main_handle)
        self._log("Closed new window/tab and switched back")

    def click_upload_next(self):
        """Click the next button after upload, retrying if the click doesn't register."""
        for attempt in range(3):
            button = self.wait.until(EC.element_to_be_clickable(self.UPLOAD_NEXT))
            button.click()
            try:
                WebDriverWait(self.driver, 5).until(EC.staleness_of(button))
                self._log("Clicked on Upload Next")
                return
            except TimeoutException:
                self._log(f"Upload Next click did not register, retrying (attempt {attempt + 1})")
        raise TimeoutException("Upload Next button click did not take effect after 3 attempts")

    def click_dox_next(self):
        self._click(self.DOX_NEXT_BUTTON, "Clicked on Dox Next Button")

    def click_pptx_next2(self):
        self._click(self.PPTX_NEXT2_BUTTON, "Clicked on PPTX Next2 Button")

    def click_test_option(self):
        self._click(self.TEST_OPTION_BUTTON, "Clicked on Test Option Button")

    def click_test_option_without(self):
        self._click(self.TEST_OPTION_WITHOUT_BUTTON, "Clicked on Test Option Without Button")

    def click_close_image(self):
        self._click(self.CLOSE_IMAGE_BUTTON, "Clicked on Close Image Button")

    def click_test_submit(self):
        self._click(self.TEST_SUBMIT_BUTTON, "Clicked on Test Submit Button")

    def click_content_next(self):
        self._click(self.CONTENT_NEXT_BUTTON, "Clicked on Content Next Button")

    def click_visit_link(self):
        self._click(self.VISIT_LINK_BUTTON, "Clicked on Visit Link Button")
