from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException




class BasePage:
    # CONSTANTS
    BASE_URL = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser: WebDriver, url: str, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
