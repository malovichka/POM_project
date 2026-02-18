from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # LOCATORS
    CART_ENDPOINT = "basket"
    CART_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    CART_ITEMS_LIST = (By.ID, "basket_formset")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    TEXT_EMPTY_CART_MESSAGE = "Your basket is empty."

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_cart_page(self):
        self.should_be_url(self.CART_ENDPOINT)
        self.is_element_present(*self.CART_HEADER)
        header = self.get_element_text(*self.CART_HEADER).lower()
        assert (
            self.CART_ENDPOINT == header
        ), f"Cart page header has text {header}, expected: {self.CART_ENDPOINT}"

    def should_not_be_any_products_added_in_cart(self):
        self.is_element_not_present(*self.CART_ITEMS_LIST)

    def should_be_empty_cart_message(self):
        self.is_element_present(*self.EMPTY_CART_MESSAGE)
        cart_message = self.get_element_text(*self.EMPTY_CART_MESSAGE)
        assert (
            self.TEXT_EMPTY_CART_MESSAGE in cart_message
        ), f"Expected to see text '{self.TEXT_EMPTY_CART_MESSAGE}' in empty cart, actual text: {cart_message}"

    def should_be_empty_cart(self):
        self.should_not_be_any_products_added_in_cart()
        self.should_be_empty_cart_message()
