from selenium.webdriver.remote.webdriver import WebDriver
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest


@pytest.mark.xfail(reason="should be failing")
def test_guest_cannot_see_success_message_after_adding_product_to_cart(
    browser: WebDriver,
):
    product_page = ProductPage(browser, BasePage.PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_show_success_message()


def test_guest_cannot_see_success_message(browser: WebDriver):
    product_page = ProductPage(browser, BasePage.PRODUCT_URL)
    product_page.open()
    product_page.should_not_show_success_message()


@pytest.mark.xfail(reason="should be failing")
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    product_page = ProductPage(browser, BasePage.PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_disappear_success_message()


def test_guest_cannot_see_product_in_cart_opened_from_product_page(browser: WebDriver):
    product_page = ProductPage(browser, BasePage.PRODUCT_URL)
    product_page.open()
    product_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.should_be_empty_cart()
