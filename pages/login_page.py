from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class LoginPage:

    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(Config.BASE_URL)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()