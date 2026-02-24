from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    title = (By.CLASS_NAME, "title")
    add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.title)
        ).text

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_backpack_button)
        ).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
