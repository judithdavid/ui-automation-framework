from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from config.config import Config

def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.USERNAME, Config.PASSWORD)

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"
