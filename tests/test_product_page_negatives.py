from selenium.webdriver.remote.webdriver import WebDriver
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest


@pytest.mark.xfail(reason="should be failing")
def test_guest_cannot_see_success_message_after_adding_product_to_cart(browser: WebDriver):
    product_page = ProductPage(browser, BasePage.BASIC_PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_not_show_success_message()

def test_guest_cannot_see_success_message(browser: WebDriver):
    product_page = ProductPage(browser, BasePage.BASIC_PRODUCT_URL)
    product_page.open()
    product_page.should_not_show_success_message()

@pytest.mark.xfail(reason="should be failing")
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    product_page = ProductPage(browser, BasePage.BASIC_PRODUCT_URL)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.should_disappear_success_message()