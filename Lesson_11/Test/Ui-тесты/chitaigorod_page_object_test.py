import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_chitay_gorod(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()

@allure.title("Поиск на кириллице")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_rus_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.rus_search('Мастер и Маргарита')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:52] == "Показываем результаты по запросу «мастер и маргарита"

@allure.title("Поиск на латинице")
@allure.description("Тест проверяет поиск книги на английском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_eng_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser) 
         main_page.set_cookie_policy()
         text = main_page.eng_search('Harry Potter and the philosophers stone')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:74] == "Показываем результаты по запросу «harry potter and the philosophers stone»"

@allure.title("Пустой поиск")
@allure.description("Тест проверяет вылонение пустого поиска")
@allure.feature("READ")
@allure.severity("trivial")
@pytest.mark.negative_test 
def test_empty_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser) 
         main_page.set_cookie_policy()
         main_page.empty_search("")
    with allure.step("Отсутствие действия на сайте"):
         url = browser.current_url
    assert url == "https://www.chitai-gorod.ru/"

@allure.title("Поиск по двум книгам")
@allure.description("Тест проверяет корректное выполнение поиска сразу по нескольким книгам")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_books_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.books_search('Бесприданница, Золушка') 
    with allure.step("Проверка текста с результатами поиска на странице "):
        assert text[0:56] == "Показываем результаты по запросу «бесприданница золушка»"

@allure.title("Поиск по категории")
@allure.description("Тест проверяет корректное выполнение поиска по категории книг")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_series_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.series_search('Книги для детей') 
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:50] == "Показываем результаты по запросу «книги для детей»"

@allure.title("Просмотр акций")
@allure.description("Тест проверяет открытие страницы с промоакциями")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_promo():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.promotions()
    with allure.step("Проверка текста с результатами поиска на странице"):
         url = browser.current_url
    assert url == "https://www.chitai-gorod.ru/promotions"

@allure.title("Поиск по каталогу")
@allure.description("Тест проверяет корректное выполнение поиска, используя каталог")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_catalog_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.catalog_search() 
    with allure.step("Проверка текста в выбранной категории каталога"):
        assert text[0:14] == 'ПОЭЗИЯ И СТИХИ'

@allure.title("Поиск по фильтру")
@allure.description("Тест проверяет корректное выполнение поиска, используя фильтр")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_filter_online():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.filter_online('Белый Клык')
    with allure.step("Проверка текста с результатами поиска на странице, отфильтрованным по новым"):
        assert text[0:42] == "Показываем результаты по запросу «айвенго»"
        
@allure.title("Проверка пустой корзины")
@allure.description("Тест проверяет, что в пустой корзине воникает сообщение 'В корзине ничего нет'")
@allure.feature("")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_get_empty_result_message():
    with allure.step("Открытие веб-страницы в Chrome"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        main_page.set_cookie_policy() 
    with allure.step("Проверка пустой корзины с сообщением 'В корзине ничего нет'"):
        msg = main_page.get_empty_result_message()
        assert msg == "В корзине ничего нет"
    with allure.step("Зактытие браузера"):
        main_page.close_driver()