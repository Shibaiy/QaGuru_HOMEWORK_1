import time

from selene import browser, be, have

def test_google_search(browser_open):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_yahoo_search(browser_open):
    browser.open('https://search.yahoo.com/')
    browser.element('[type=text]').should(be.blank).type('Балтика 9').press_enter()
    browser.element('[id=main]').should(have.text('Балтика 9: состав'))


def test_yahoo_searh_noresult(browser_open):
    browser.open('https://search.yahoo.com/')
    browser.element('[type=text]').should(be.blank).type('asdfgq123vddd').press_enter()
    browser.element('[class="first last"]').should(have.text('We did not find results for: '))






