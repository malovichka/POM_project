from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage



class MainPage(BasePage):
    #LOCATORS
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Login Link is not present"

    def go_to_login_page(self) -> None:
        login_link = self.browser.find_element(*self.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()


