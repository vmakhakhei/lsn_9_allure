import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url = "http://github.com"
repository = 'vmakhakhei/lsn_9_allure'

def test_dynamic_steps():
    with allure.step('Открываем github'):
        browser.open(url)
    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').type(repository)
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('vmakhakhei/lsn_9_allure')).click()
    with allure.step('Открывает табу Issue'):
        s('#issues-tab').click()
    with allure.step('Ищем issue с номером #1'):
        s(by.partial_text('#1')).should(be.visible)
