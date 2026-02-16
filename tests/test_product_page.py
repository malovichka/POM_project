from selenium.webdriver.remote.webdriver import WebDriver
from pages.product_page import ProductPage
from pages.base_page import BasePage
import pytest


def test_quest_can_add_product_to_basket(browser: WebDriver):
    """
    Verify that a guest user can add a product to the basket from a promotion page.

    Steps:
    1. Open the product page with a promotion parameter.
    2. Verify the page is correctly loaded as a promotion page.
    3. Capture the current cart total before any action.
    4. Click 'Add to basket' button.
    5. Solve the browser alert quiz to confirm the addition.
    6. Verify success messages and that the cart total increased by the product price.
    """
    product_page = ProductPage(browser, ProductPage.PROMO_URL)
    product_page.open()
    product_page.should_be_promotion_page()
    cart_total_before_adding = product_page.get_cart_total()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_added_to_cart(cart_total_before_adding)


@pytest.mark.parametrize("promo_url", BasePage.PROMO_LINKS)
def test_guest_can_add_product_to_basket_with_promo(browser: WebDriver, promo_url):
    """
    Verify that a guest user can add a product to the basket from a promotion page.

    Steps:
    1. Open the product page with a promotion parameter.
    2. Verify the page is correctly loaded as a promotion page.
    3. Capture the current cart total before any action.
    4. Click 'Add to basket' button.
    5. Solve the browser alert quiz to confirm the addition.
    6. Verify success messages and that the cart total increased by the product price.
    """
    product_page = ProductPage(browser, promo_url)
    product_page.open()
    product_page.should_be_promotion_page()
    cart_total_before_adding = product_page.get_cart_total()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_added_to_cart(cart_total_before_adding)
