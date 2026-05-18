import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.regression
def test_invalid_login(driver):

    login_page = LoginPage(driver)

    login_page.load()

    login_page.login(
        "invalid_user",
        "invalid_password"
    )

    error_text = login_page.get_error_message()

    assert error_text == (
        "Epic sadface: Username and password "
        "do not match any user in this service"
    )


@pytest.mark.regression
def test_cart_should_not_contain_unadded_item(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    login_page.load()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.open_cart()

    assert cart_page.is_item_present() is False