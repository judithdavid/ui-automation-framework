from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from selenium.webdriver.remote.webelement import WebElement

import time

from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException
)

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(__name__)


    def click(self, locator, retries=2):

        for attempt in range(retries + 1):

            try:

                self.logger.info(
                    f"Clicking element: {locator}"
                )

                self.wait_for_clickable(locator).click()

                return

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException
            ) as e:

                self.logger.warning(
                    f"Retrying click for {locator} "
                    f"| Attempt {attempt + 1}"
                )

                time.sleep(1)

        self.logger.error(
            f"Failed to click element after retries: {locator}"
        )

        raise
    
    def type(self, locator, text):

        self.logger.info(f"Typing into element: {locator}")

        element = self.wait_for_visibility(locator)

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

    def wait_for_visibility(self, locator) -> WebElement:

        self.logger.debug(
            f"Waiting for visibility: {locator}"
        )

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )


    def wait_for_clickable(self, locator) -> WebElement:

        self.logger.debug(
            f"Waiting for clickable element: {locator}"
        )

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
    
    def is_element_visible(self, locator, timeout=5):

        try:

            WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except Exception:

            return False
        
    def get_page_title(self):

        self.logger.debug(
            "Fetching browser title"
        )

        return self.driver.title