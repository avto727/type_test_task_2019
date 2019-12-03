from page import *
from time import sleep
# Предусловие - "
# Скрипт выполняет авторизацию на сайте https://master.edo-paritet.ru:9443, заполняет бланк заявки, logout.

def case_paritet(self):
    login = "manag3"
    passw = '12345678'
    print('\n Запуск Тест кейс № 1 login \n')
    email = "avto727@bk.ru"
    passw = '6bacf7f58583'
    self.page.login_servers_com(email, passw)
    email_user = self.result.find_link('email_user')
    assert (email) == email_user
    print('Авторизация подтверждена')
    sleep(1)
    self.page.logout()
