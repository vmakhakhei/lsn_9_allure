from selene import by, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url = "http://github.com"
repository = 'vmakhakhei/lsn_9_allure'

def test_github():
    browser.open(url)

    s('.header-search-input').click()
    s('.header-search-input').type(repository)
    s('.header-search-input').submit()

    s(by.link_text('vmakhakhei/lsn_9_allure')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)


