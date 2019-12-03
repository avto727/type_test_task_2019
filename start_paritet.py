import pytest
from selenium import webdriver
from test_case_paritet import test_case_paritet
from page import *


class Test_paritet():

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://master.edo-paritet.ru:9443")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.page = MainPage(self.driver)
        self.prof = Profile(self.driver)
        self.result = ResultPage(self.driver)
        self.admin = Admin(self.driver)

        self.full_screen = 0

    def teardown(self):
        self.driver.close()

    def test_case_paritet(self):
        case_paritet(self)


