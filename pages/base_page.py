from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(__name__)

    def click(self, locator):

        self.logger.info(f"Clicking element: {locator}")

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
    
    def type(self, locator, text):

        self.logger.info(f"Typing into element: {locator}")

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):

        self.logger.info(f"Getting text from: {locator}")

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def open(self, url):

        self.logger.info(f"Opening URL: {url}")

        self.driver.get(url)