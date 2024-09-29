import allure
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

base_url = "https://web-gate.chitai-gorod.ru/api"

headers = { 

        'content-type': 'application/json',
        'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc2MjI3NDcsImlhdCI6MTcyNzQ1NDc0NywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjA2YTkwNTA2NTZjMDRhOGFlM2E0ZTRjZmY4N2NmYzIwZjFiZGM5ODM1ZDg2NmQwNWNhNDFlYjU4NGU0MjMyMjEiLCJ0eXBlIjoxMH0.hS34YtGVUAxDe-taYvIw-2RELNrf7FP5495E-8bFXSg"
         
    }

@allure.title("Поиск по одному слову")
@allure.description("Тест проверяет корректный поиск книги по одному слову")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_russian_lang():
    
    with allure.step("api. Поиск по одному слову через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=гарри', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

@allure.title("Поиск по нескольким словам")
@allure.description("Тест проверяет корректный поиск книги по нескольким словам")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_russian_lang_two_words():
    with allure.step("api. Поиск по нескольким словам через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=гарри поттер', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

@allure.title("Поиск по автору")
@allure.description("Тест проверяет корректный поиск книги по автору")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_author():
    with allure.step("api. Поиск по автору через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=Джоан Роулинг', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

@allure.title("Поиск по серии")
@allure.description("Тест проверяет корректный поиск книги по серии")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_series():
    with allure.step("api. Поиск по серии через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=Дозоры', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"

@allure.title("Поиск по жанру")
@allure.description("Тест проверяет корректный поиск книги по жанру")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_genre():
    with allure.step("api. Поиск по жанру через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=Любовный роман', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"

@allure.title("Поиск по латинице")
@allure.description("Тест проверяет корректный поиск книги на английском")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_eng():
    with allure.step("api. Поиск на латинице через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=Harry Potter', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"

@allure.title("Поиск канцелярии")
@allure.description("Тест проверяет корректный поиск сопутствующих товаров на сайте")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_alt_products():
    with allure.step("api. Поиск сопутствующих товаров через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=Канцелярия', headers=headers)
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"

@allure.title("Негативная проверка поиска с DELETE")
@allure.description("Отправка запроса поиска с канцелярии с неверным методом DELETE")
@allure.feature("DELETE")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_alt_products_del():
    with allure.step("api. Отправка запроса поиска с неверным методом DELETE через API и получение ошибки 405"):
        resp = requests.delete(base_url+'/v2/search/facet-search?customer&phrase=Канцелярия', headers=headers)
        assert resp.headers["Content-Type"] == "text/plain"
        assert resp.status_code == 405

@allure.title("Негативная проверка ввода в поиск знаков препинания")
@allure.description("Тест проверяет, что сайт выдаёт ошибку при вводе знаков препинания")
@allure.feature("READ")
@allure.severity("minor")
@pytest.mark.negative_test
def test_coma():
    with allure.step("api. Отправка запроса со знаками препинания через API, в ответе:Недопустимая поисковая фраза "):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=,,,', headers=headers)
        assert resp.headers["Content-Type"] == "application/json"
        assert 'Недопустимая поисковая фраза' in resp.text 

@allure.title("Пустой поиск")
@allure.description("Тест проверяет ответ: 'Phrase должен содержать минимум 2 символа")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.negative_test
def test_empty():
    with allure.step("api. Отправка пустого поиска с ответом: Phrase должен содержать минимум 2 символа через API"):
        resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase= ', headers=headers)
        assert resp.headers["Content-Type"] == "application/json"
        assert 'Phrase должен содержать минимум 2 символа' in resp.text