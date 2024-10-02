from selene import browser, be, have

def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
    browser.quit()

def test_yahoo_search():
    browser.open('https://search.yahoo.com/')
    browser.element('[type=text]').should(be.blank).type('Балтика 9').press_enter()
    browser.element('[id=main]').should(have.text('Балтика 9: состав'))
    browser.quit()




