import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Iterator


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="choose browser: chorme or firefox",
    )

    parser.addoption(
        "--no-incognito",
        action="store_false",
        dest="incognito",
        default=True,
        help="disable incognito mode (enabled by default)",
    )

    parser.addoption(
        "--headless", action="store_true", help="run browser in headless mode"
    )

    parser.addoption(
        "--language", action="store", default="en", help="choose browser language"
    )


@pytest.fixture(scope="function")
def browser(request) -> Iterator[WebDriver]:
    incognito = request.config.getoption("incognito")
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    user_language = request.config.getoption("language")

    driver = None

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if incognito:
            chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if incognito:
            firefox_options.add_argument("-private")
        if headless:
            firefox_options.add_argument("-headless")
        firefox_options.set_preference("intl.accept_language", user_language)
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield driver
    driver.quit()
