
import pytest
from selene import browser

@pytest.fixture(scope='session')
def browser1():
    print('\nbrowser')
    yield
    print('\nclose browser')


@pytest.fixture(scope='session')
def browser_open():
    browser.open()
    yield
    browser.quit()