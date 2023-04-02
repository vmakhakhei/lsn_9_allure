import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url = "http://github.com"
repository = 'vmakhakhei/lsn_9_allure'
issue_number = "#1"


@allure.label('Owner, vmakhakhei')
@allure.title('Шаги с декоратором')
def test_decorator_steps():
    open_main_page()
    search_for_repository(repository)
    open_repository(repository)
    open_issue_tab()
    search_issue_by_number(issue_number)


@allure.step('Открываем github')
def open_main_page():
    browser.open(url)


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').type(repo)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория{repo}')
def open_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открывает табу Issue')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Ищем issue с номером {number}')
def search_issue_by_number(number):
    s(by.partial_text(number)).should(be.visible)
