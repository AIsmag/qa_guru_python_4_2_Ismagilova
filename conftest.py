import pytest
from selene.support.shared import browser


@pytest.fixture
def size_of_browser():
    browser.config.window_width = 1900
    browser.config.window_height = 1900


@pytest.fixture
def open_google(size_of_browser):
    browser.open('https://google.com')
