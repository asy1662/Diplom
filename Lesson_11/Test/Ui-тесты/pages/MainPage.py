import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
      def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

      with allure.step("Политика куки"):
           def set_cookie_policy(self): 
               cookie = {"name": "cookie_policy", "value": "1"}
               self._driver.add_cookie(cookie)

      with allure.step("Поиск книги на кириллице"):
           def rus_search(self,term):
               self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
               self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
               txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
               return txt

      with allure.step("Поиск книги на латинице"):
          def eng_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
              return txt
    
      with allure.step("Пустой поиск"):
          def empty_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
       
      with allure.step("Поиск сразу нескольких книг"):
            def books_search(self,term):
                self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
                self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
                txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
                return txt
      
      with allure.step("Поиск по категории"):
          def series_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
              return txt
      
      with allure.step("Поиск через каталог"):
          def catalog_search(self):
              self._driver.find_element(By.XPATH, '//div[contains(text(),"Да, я здесь")]').click()
              self._driver.find_element(By.XPATH, '//span[contains(text(),"Каталог")]').click()
              self._driver.find_element(By.XPATH, '//span[contains(text(),"Художественная литература")]').click()
              self._driver.find_element(By.XPATH, '//span[contains(text(),"Поэзия")]').click()
              txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/h1').text
              return txt

      with allure.step("Просмотр акций на странице"):
           def promotions(self):
               self._driver.find_element(By.XPATH, '//div[contains(text(),"Да, я здесь")]').click()
               self._driver.get("https://www.chitai-gorod.ru/promotions")
               

      with allure.step("Проверка пустой корзины"):
            def get_empty_result_message(self):
                self._driver.get("https://www.chitai-gorod.ru/cart")
                txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[1]').text
                return txt
      
      with allure.step("Проверка фильтра 'Сначала новые'"):
            
            def filter_online(self,term):
               self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
               self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
               txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text# выдача
               self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/div[1]/div/div[1]/div').click() #клик по релевантности
               self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/div[1]/div/div[2]/div/div[2]').click() # клик сначала новые
               return txt
            
      
      with allure.step("Закрытие веб-браузера"):
            def close_driver(self):
                self._driver.quit()