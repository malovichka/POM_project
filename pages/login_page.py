from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # LOCATORS
    LOGIN_PAGE_ENDPOINT = "accounts/login"
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.should_be_url(self.LOGIN_PAGE_ENDPOINT)

    def should_be_login_form(self):
        assert self.is_element_present(
            *self.LOGIN_EMAIL
        ), "Login email address field is missing"
        assert self.is_element_present(
            *self.LOGIN_PASSWORD
        ), "Login password field is missing"
        assert self.is_element_present(*self.LOGIN_BUTTON), "Login button is missing"

    def should_be_register_form(self):
        assert self.is_element_present(
            *self.REGISTER_EMAIL
        ), "Email input in Registration form is missing"
        assert self.is_element_present(
            *self.REGISTER_PASSWORD
        ), "Password input in Registration form is missing"
        assert self.is_element_present(
            *self.REGISTER_CONFIM_PASSWORD
        ), "Password confirmation in Registration form is missing"
        assert self.is_element_present(
            *self.REGISTER_BUTTON
        ), "Register button in Registration form is missing"
