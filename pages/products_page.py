from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):

    title = (By.CLASS_NAME, "title")
    add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_loaded(self):
        return self.get_text(self.title)

    def add_backpack_to_cart(self):
        self.click(self.add_backpack_button)

    def open_cart(self):
        self.click(self.cart_icon)
