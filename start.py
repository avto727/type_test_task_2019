import pytest
from selenium import webdriver
from test_case_1 import case_1
from test_case_2 import case_2

from page import *


class Test():

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://portal.servers.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.page = MainPage(self.driver)
        self.prof = Profile(self.driver)
        self.result = ResultPage(self.driver)
        self.admin = Admin(self.driver)

        self.full_screen = 0

    def teardown(self):
        self.driver.close()

    # def test_case_1(self):
    #     case_1(self)

    def test_case_2(self):
        case_2(self)

