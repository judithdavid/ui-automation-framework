from selenium.webdriver.common.by import By
from config.config import Config
from pages.base_page import BasePage

class LoginPage(BasePage):

    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    error_message = (
    By.CSS_SELECTOR,
    "h3[data-test='error']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open(Config.BASE_URL)

    def login(self, username, password):
        self.type(self.username_field, username)
        self.type(self.password_field, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)