import math
import re
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # CONSTANTS AND LOCATORS
    BASE_URL = "http://selenium1py.pythonanywhere.com/"
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    OLD_PROMO_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PROMO_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    PROMO_LINKS = [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail,
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ]
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_CART_BUTTON = (
        By.CSS_SELECTOR,
        ".basket-mini.hidden-xs .btn-default[href*='/basket/']",
    )

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            WebDriverWait(self.browser, self.timeout).until(
                expected_conditions.visibility_of_element_located((how, what))
            )
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, how: str, what: str) -> bool:
        """Returns True if element is NOT located within given timeout"""
        try:
            WebDriverWait(self.browser, self.timeout).until(
                expected_conditions.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_element_gone(self, how: str, what: str) -> bool:
        try:
            WebDriverWait(self.browser, self.timeout, 1).until_not(
                expected_conditions.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def get_element_text(self, how: str, what: str) -> str:
        self.is_element_present(how, what)
        return self.browser.find_element(how, what).text.strip()

    def get_price_from_text(self, how: str, what: str) -> float:
        text = self.get_element_text(how, what)
        price = re.search(r"\d+\.\d+", text)
        assert price, f"Could not extract price value from text: {text}"
        return float(price.group())

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"THE CODE IS HERE: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_url(self, endpoint: str):
        assert (
            endpoint in self.browser.current_url
        ), f"Expected {endpoint} missing in current URL: {self.browser.current_url}"

    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), "Login Link is not present"

    def go_to_login_page(self) -> None:
        self.is_element_present(*self.LOGIN_LINK)
        self.browser.find_element(*self.LOGIN_LINK).click()

    def go_to_cart_page(self) -> None:
        self.is_element_present(*self.VIEW_CART_BUTTON)
        self.browser.find_element(*self.VIEW_CART_BUTTON).click()
