from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    """Page object for the Kiosk Home Page, handling visitor check-in flow."""

    # Optional loader locator (update if your app uses one)
    LOADER = (By.CLASS_NAME, "loader")

    # Locators for UI elements
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
    HOST_INPUT = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/div/div/div/div/div[1]/div")
    HOST_NEXT = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[3]/div/button[2]")
    # Default upload locator and file path
    UPLOAD_BUTTON = "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[1]/button"
    UPLOAD_FILE_PATH = r"C:\Users\AbdulRafay\Downloads\1380678.jpg"
    UPLOAD_NEXT = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/button")
    DOX_NEXT_BUTTON = (
        By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div/button")
    PPTX_NEXT2_BUTTON = (
        By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div/div/button")
    TEST_OPTION_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/button/div")                   
    TEST_OPTION_WITHOUT_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/button")
    CLOSE_IMAGE_BUTTON = (
        By.XPATH, "/html/body/div[3]/div[4]")
    TEST_SUBMIT_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/button")  
    CONTENT_NEXT_BUTTON = (
        By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/button") 
    
    def __init__(self, driver, logger=None):
        """Initialize the HomePage with driver and optional logger."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 100, poll_frequency=3)  # Retry every 3 seconds
        self.logger = logger

    def _log(self, message):
        """Log a message if logger is provided."""
        if self.logger:
            self.logger(message)

    def wait_for_api(self, timeout=100):
        """Wait for page to load and API calls to complete."""
        try:
            # Wait for DOM ready
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            # Wait for loader to disappear if present
            try:
                WebDriverWait(self.driver, 100).until(
                    EC.invisibility_of_element_located(self.LOADER)
                )
            except TimeoutException:
                pass  # Loader not present, ignore
            self._log("API completed successfully")
        except TimeoutException:
            self._log("API timeout exceeded")
            raise

    def open(self):
        """Open the home page URL."""
        self.driver.get("https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/home")
        self._log("Opened home page")

    def home_url(self):
        """Return the expected home URL."""
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/home"

    def click_check_in(self):
        """Click the Check In button."""
        self.wait.until(EC.element_to_be_clickable(self.CHECK_IN_BUTTON)).click()
        self._log("Clicked Check In button")

    def visitor_type_url(self):
        """Return the expected visitor type URL."""
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/visitor-type"

    def click_chose_workflow(self):
        """Click the chose workflow option."""
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_WORKFLOW)).click()
        self._log("Chose workflow clicked")

    def num_people_url(self):
        """Return the expected num people URL."""
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/num-people"

    def click_next_multiparty(self):
        """Click the next button for multiparty."""
        self.wait.until(EC.element_to_be_clickable(self.NEXT_MULTIPARTY)).click()
        self._log("Next button clicked")

    def visitor_info_url(self):
        """Return the expected visitor info URL."""
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/visitor-info"

    def phone_input(self):
        """Enter phone number."""
        self.wait.until(EC.element_to_be_clickable(self.PHONE_INPUT)).send_keys("3021843163")
        self._log("Phone number entered")

    def click_phone_next(self):
        """Click the next button after phone input."""
        self.wait.until(EC.element_to_be_clickable(self.PHONE_Next)).click()
        self.wait_for_api()
        self._log("Phone Next button clicked")

    def chose_profile(self):
        """Choose the first profile."""
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_PROFILE)).click()
        self.wait_for_api()
        self._log("Clicked on Profile")

    def chose_host_url(self):
        """Return the expected choose host URL."""
        return "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/choose-host"

    def click_chose_host(self):
        """Click the chose host option."""
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_HOST)).click()
        self._log("Clicked on Search Host icon")

    def click_host_next(self):
        """Click the next button after choosing host."""
        self.wait.until(EC.element_to_be_clickable(self.HOST_NEXT)).click()
        self._log("Clicked on Host Next")

    def upload_file(self, upload_xpath: str = None, file_path: str = None, timeout: int = 30):
        """Upload a file using the provided xpath/button.

        Behavior:
        - First, try to find an `input[type=file]` anywhere on the page and send the file path directly (avoids opening native dialog).
        - If no input found, click the provided element to potentially reveal it, then find and send.
        - If the provided xpath is directly an input[type=file], send directly.

        Note: Selenium cannot interact with native OS file dialogs. Sending
        a path to an `input[type=file]` avoids opening the OS dialog.
        """
        # Use provided values or fall back to class defaults
        upload_xpath = upload_xpath or getattr(self, 'UPLOAD_BUTTON', None)
        file_path = file_path or getattr(self, 'UPLOAD_FILE_PATH', None)
        if not upload_xpath or not file_path:
            raise ValueError('upload_xpath and file_path must be provided either as args or set on the page object')

        locator = (By.XPATH, upload_xpath)
        el = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

        try:
            tag = el.tag_name.lower()
        except Exception:
            tag = ''

        input_type = (el.get_attribute('type') or '').lower()

        # If the element itself is a file input, send the file path directly
        if tag == 'input' and input_type == 'file':
            el.send_keys(file_path)
            self._log(f"Uploaded file: {file_path}")
            return

        # First, try to find any input[type=file] on the page without clicking
        try:
            file_input = WebDriverWait(self.driver, 5).until(  # Short wait
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            file_input.send_keys(file_path)
            self._log(f"Uploaded file via existing input: {file_path}")
            return
        except Exception:
            pass  # No input found, proceed to click

        # Otherwise attempt to click the provided element to reveal the file input
        try:
            el.click()
        except Exception:
            try:
                self.driver.execute_script("arguments[0].click();", el)
            except Exception:
                pass

        # Now try to find any input[type=file] in DOM after click
        try:
            file_input = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
            )
            file_input.send_keys(file_path)
            self._log(f"Uploaded file via discovered input: {file_path}")
            return
        except Exception:
            pass

        # Try nested input under the clicked element as a last resort
        try:
            nested = el.find_element(By.XPATH, ".//input[@type='file']")
            nested.send_keys(file_path)
            self._log(f"Uploaded file via nested input: {file_path}")
            return
        except Exception:
            pass

        raise Exception(
            "Could not find an input[type=file] to upload the file. "
            "If your UI uses a native file dialog, locate a hidden file input and pass its xpath."
        )

    def click_upload_next(self):
        """Click the next button after upload."""
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_NEXT)).click()
        self._log("Clicked on Upload Next")

    def click_dox_next(self):
        """Click the next button on dox page."""
        self.wait.until(EC.element_to_be_clickable(self.DOX_NEXT_BUTTON)).click()
        self._log("Clicked on Dox Next Button")

    def click_pptx_next2(self):
        """Click the next button on pptx page."""
        self.wait.until(EC.element_to_be_clickable(self.PPTX_NEXT2_BUTTON)).click()
        self._log("Clicked on PPTX Next2 Button")

    def click_test_option(self):
        """Click the test option button."""
        self.wait.until(EC.element_to_be_clickable(self.TEST_OPTION_BUTTON)).click()
        self._log("Clicked on Test Option Button")

    def click_test_option_without(self):
        """Click the test option without button."""
        self.wait.until(EC.element_to_be_clickable(self.TEST_OPTION_WITHOUT_BUTTON)).click()
        self._log("Clicked on Test Option Without Button")    

    def click_close_image(self):
        """Click the close image button."""
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_IMAGE_BUTTON)).click()
        self._log("Clicked on Close Image Button")

    def click_test_submit(self):
        """Click the test submit button."""
        self.wait.until(EC.element_to_be_clickable(self.TEST_SUBMIT_BUTTON)).click()
        self._log("Clicked on Test Submit Button")    

    def click_content_next(self):
        """Click the content next button."""
        self.wait.until(EC.element_to_be_clickable(self.CONTENT_NEXT_BUTTON)).click()
        self._log("Clicked on Content Next Button")
