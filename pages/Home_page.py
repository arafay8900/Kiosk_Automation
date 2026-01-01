from multiprocessing.managers import Value

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    # Optional loader locator (update if your app uses one)
    LOADER = (By.CLASS_NAME, "loader")  # change if needed

    def wait_for_api(self, timeout=100):
        try:
            # 1️⃣ Wait for DOM ready
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            # 2️⃣ Wait for loader to disappear (if exists)
            try:
                WebDriverWait(self.driver, 100).until(
                    EC.invisibility_of_element_located(self.LOADER)
                )
            except TimeoutException:
                pass  # Loader not present, ignore

            self._log("⏳ API completed successfully")

        except TimeoutException:
            self._log("❌ API timeout exceeded")
            raise



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


    def __init__(self, driver, logger=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 100)
        self.logger = logger  # pass the logger fixture here

    def _log(self, message):
        if self.logger:
            self.logger(message)

    def open(self):
        self.driver.get("https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/home")
        self._log("✅ Opened home page")

    def home_url(self):
        expected_url = "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/home"
        self._log(f"Verify URL: {expected_url}")
        return expected_url

    def click_check_in(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_IN_BUTTON)).click()
        self._log("✅ Clicked Check In button")

    def visitor_type_url(self):
        expected_url = "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/visitor-type"
        self._log(f"Verify URL: {expected_url}")
        return expected_url

    def click_chose_workflow(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_WORKFLOW)).click()
        self._log("✅ Chose workflow clicked")

    def num_people_url(self):
        expected_url = "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/num-people"
        self._log(f"Verify URL: {expected_url}")
        return expected_url

    def click_next_multiparty(self):
        self.wait.until(EC.element_to_be_clickable(self.NEXT_MULTIPARTY)).click()
        self._log("✅ Next button clicked")

    def visitor_info_url(self):
        expected_url = "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/visitor-info"
        self._log(f"Verify URL: {expected_url}")
        return expected_url

    def phone_input(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_INPUT)).send_keys("3021843163")
        self._log("✅ Phone number entered")

    def click_phone_next(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_Next)).click()
        self.wait_for_api()
        self._log("✅ Phone Next button clicked")

    def chose_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_PROFILE)).click()
        self.wait_for_api()
        self._log("✅ Clicked on Profile")

    def chose_host_url(self):
        expected_url = "https://app.undesked.com/kiosk/1a3f9f5c-753f-4344-a7d9-8269e0001d14/choose-host"
        self._log(f"Verify URL: {expected_url}")
        self.wait_for_api()
        return expected_url

    def click_chose_host(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOSE_HOST)).click()
        self._log("✅ Clicked on Search Host icon")

    def click_host_next(self):
        self.wait.until(EC.element_to_be_clickable(self.HOST_NEXT)).click()
        self._log("✅ Clicked on Host Next")
