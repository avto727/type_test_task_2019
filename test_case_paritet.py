from page import *
from time import sleep
# Предусловие - "
# Скрипт выполняет авторизацию на сайте https://master.edo-paritet.ru:9443, заполняет бланк заявки, logout.

def case_paritet(self):
    login = "manag3"
    passw = '12345678'
    print('\n Запуск Тест кейс № 1 login \n')
    self.page.login_paritet(login, passw)
    valid_text = self.result.find_text('Создать')
    assert ('СОЗДАТЬ') == valid_text
    print('Авторизация подтверждена')
