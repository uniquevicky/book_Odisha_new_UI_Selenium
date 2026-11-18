
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from config.config import EXPLICIT_WAIT


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,EXPLICIT_WAIT)

    # Wait until element is visible
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator))

    # Wait until element is clickable
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Find element
    def find_element(self, locator):
        return self.wait_for_visibility(locator)

    # Find multiple elements
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # Click element
    def click_element(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    # Enter text
    def enter_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    # Get element text
    def get_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text.strip()

    # Verify element visibility
    def is_element_displayed(self, locator):
        try:
            element = self.wait_for_visibility(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    # Verify element is enabled
    def is_element_enabled(self, locator):
        element = self.wait_for_visibility(locator)
        return element.is_enabled()

    # Navigate to URL
    def navigate_to(self, url):
        self.driver.get(url)

    # Get current URL
    def get_current_url(self):
        return self.driver.current_url

    # Get page title
    def get_page_title(self):
        return self.driver.title
