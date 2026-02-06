from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser: WebDriver):
    browser.get(BasePage.BASE_URL)
    browser.find_element(*MainPage.LOGIN_LINK).click()
    time.sleep(7)