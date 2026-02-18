from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # LOCATORS
    PROMO_PARAM = "?promo="
    CART_TOTAL_HEADER = (By.CLASS_NAME, "basket-mini")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_PRODUCT_ADDED = (
        By.CSS_SELECTOR,
        "#messages .alert:first-of-type .alertinner",
    )
    MESSAGE_CART_TOTAL = (By.CSS_SELECTOR, "#messages .alert:last-of-type .alertinner")

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        super().__init__(browser, url, timeout)

    def should_be_promotion_page(self):
        assert (
            self.PROMO_PARAM in self.browser.current_url
        ), f"Promo parameter is absent, current URL is {self.browser.current_url}"

    def get_cart_total(self) -> float:
        return self.get_price_from_text(*self.CART_TOTAL_HEADER)

    def add_product_to_cart(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()

    def should_be_product_added_to_cart(self, cart_total_before):
        product_name = self.get_element_text(*self.PRODUCT_NAME)
        print(f"PRODUCT NAME {product_name}")
        product_price = self.get_price_from_text(*self.PRODUCT_PRICE)
        print(f"PRODUCT PRICE {product_price}")
        self.should_be_message_about_adding_product(product_name)
        self.should_be_message_with_cart_total(product_price, cart_total_before)

    def should_be_message_about_adding_product(self, product_name: str):
        self.is_element_present(*self.MESSAGE_PRODUCT_ADDED)
        message = self.get_element_text(*self.MESSAGE_PRODUCT_ADDED)
        expected_message = f"{product_name} has been added to your basket."
        print(f"ALERT TEXT IS {message}")
        assert (
            message == expected_message
        ), f"Alert actual text is: {message}. Should be: {expected_message}"

    def should_be_message_with_cart_total(
        self, added_product_price: float, cart_total_before: float
    ):
        self.is_element_present(*self.MESSAGE_CART_TOTAL)
        expected_total = cart_total_before + added_product_price
        message_total = self.get_price_from_text(*self.MESSAGE_CART_TOTAL)
        header_total = self.get_cart_total()
        assert (
            message_total == expected_total
        ), f"Cart total should be {expected_total}, got {message_total} in message instead"
        assert (
            header_total == expected_total
        ), f"Cart total in header should be {expected_total}, got {header_total} instead"

    def should_not_show_success_message(self):
        assert self.is_element_not_present(
            *self.MESSAGE_PRODUCT_ADDED
        ), "Success alert is present, and it should not be"

    def should_disappear_success_message(self):
        assert self.is_element_gone(
            *self.MESSAGE_PRODUCT_ADDED
        ), "Success alert did not disappear in given timeout"
