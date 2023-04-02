from selene import by, be
from selene.support.shared import browser

url = "http://github.com"
page = 'vmakhakhei?tab=repositories'
repository = 'lsn_9_allure'

def test_github():
    browser.open(url)
    browser.element('.header-search-input').click().type('eroshenkoam/allure-example').press_enter()

