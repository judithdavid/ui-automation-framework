from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):

    cart_item_name = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item_name(self):
        return self.get_text(self.cart_item_name)

    def is_item_present(self):

        try:
            self.get_text(self.cart_item_name)
            return True

        except TimeoutException:
            return False