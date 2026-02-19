from selenium.webdriver.remote.webdriver import WebDriver
from pages.cart_page import CartPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser: WebDriver):
        main_page = MainPage(browser, BasePage.BASE_URL)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser: WebDriver):
        main_page = MainPage(browser, BasePage.BASE_URL)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cannot_see_product_in_cart_opened_from_main_page(browser: WebDriver):
    main_page = MainPage(browser, BasePage.BASE_URL)
    main_page.open()
    main_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.should_be_empty_cart()


