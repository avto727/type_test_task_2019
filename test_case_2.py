from page import *
from time import sleep
# Предусловие - "
# Скрипт выполнЕт авторизацию на сайте https://portal.servers.com

def case_2(self):
    print('\n Запуск Тест кейс № 2 Create order \n')
    email = "ask_ev_avto727@mail.ru"
    passw = '9367ccdfb86a'
    self.page.login_servers_com(email, passw)
    self.page.click_f('Клик_Dedicated_Servers', 1)
    self.page.click_f('Клик_Order_Dedicated_Servers', 2, 1)
    self.page.click_f('Клик_Order_now', 3, 0)
    self.page.click_f('Swap_Free_of_charge', 4, 7)
    self.page.click_f('Клик_check_box_OS', 5, 7)
    self.page.click_f('Swap_Install_add_ons', 6)
    self.page.click_f('Клик_check_box_SSH', 7, 21)
    self.page.click_f('Swap_Install_add_ons', 6)
    self.page.click_f('Клик_1_TB_SATA3_3_5', 8)
    self.page.click_f('Клик_check_box_OS', 9, 23)
    self.page.click_f('Swap_hostname', 10)
    self.page.send_f('Ввод_hostname', 'test.com', 11)
    sleep(1)
    self.page.click_f('Клик_Add_to_card', 12)
    sleep(2)
    self.page.click_f('Swap_email_login', 13)
    self.page.logout()
