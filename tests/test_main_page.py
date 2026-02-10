from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser: WebDriver):
    main_page = MainPage(browser, MainPage.BASE_URL)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(7)


def test_guest_should_see_login_link(browser: WebDriver):
    main_page = MainPage(browser, MainPage.BASE_URL)
    main_page.open()
    main_page.should_be_login_link()
    time.sleep(5)
