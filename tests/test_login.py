from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.config import Config

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)

    products_page = ProductsPage(driver)
    assert products_page.verify_loaded() == "Products"
