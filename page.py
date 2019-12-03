import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
"""File Page Object Model"""

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class ResultPage(BasePage):

    # Найти подтверждающий элемент
    def find_link(self, name):
        page = MainPage(self.driver)
        resx = {
            'email_user': {'tag_': 'div', 'class_': 'CurrentUserWidget-sc-1xtml1f-0 VMdDP'},
        }
        path = './/ttag[@class="cclass"]'
        path_1 = path.replace('ttag', resx[name]['tag_'])
        xpath = path_1.replace('cclass', resx[name]['class_'])
        # page.waitForElementVisible(xpath, 7)
        time.sleep(2)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        # print('Это суп', soup)
        ls = soup.find(resx[name]['tag_'], resx[name]['class_']).text
        # print(ls)
        return ls

    def find_text(self, find, index=0):
        page = MainPage(self.driver)
        dir_f = {
            "Создать": './/a[@class="action-btn--edit user-edit"]',
        }
        xpath = dir_f.get(find)
        page.waitForElementClickable(xpath, 12)
        text = self.driver.find_elements_by_xpath(xpath)[index].text
        return text

class Admin(BasePage):

    def click_f(self, name, stap):
        page = MainPage(self.driver)
        step = str(stap)
        self.adminx = {
            'Профили_посетителей': {'func': page.click_xpath, 'path': './/a[text()="Профили посетителей"]'},

        }
        #'': {'func': '', 'path': ''}
        self.args = self.adminx[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
# эти клики еще не внесены в словарь (((


class Profile(BasePage):
    def click_f(self, name, step_int):
        result = ResultPage(self.driver)
        page = MainPage(self.driver)
        step = str(step_int)
        self.profx = {
            'Клик_Зарегистрироваться': {'func': page.click_id, 'path': 'register-email-submit'},
            'Клик_Сохранить': {'func': page.click_xpath, 'path': './/button[text()="Сохранить"]'},
            'Клик_Избранное': {'func': page.click_xpath, 'path': './/a[text()="Избранное"]'},

        }
        # Profile
        self.args = self.profx[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')

class MainPage(BasePage):
    def click_f(self, name, stap, index=0):
        step = str(stap)
        self.pagex = {
    'Клик_Dedicated_Servers': {'func': self.click_xpath,'path': './/span[text()="Dedicated Servers"]'},
    'Клик_Order_Dedicated_Servers': {'func': self.click_xpath,'path': './/a[@class="Link-otujlc-0 hxslCu"]'},
    'Клик_Order_now': {'func': self.click_xpath,'path': './/button[@class="btn btn-danger btn-primary ng-binding"]'},
    'Клик_Вход_Signin': {'func': self.click_xpath,'path': './/button[@class="btn btn-dark text-left"]'},
    'Клик_check_box_OS': {'func': self.click_xpath,'path': './/div[@class="styles__radio___1Lchd"]'},
    'Клик_check_box_SSH': {'func': self.click_xpath,'path': './/div[@class="styles__radio___1Lchd"]'},
    'Клик_Add_to_card': {'func': self.click_xpath, 'path': './/span[text()="Add to cart"]'},
    'Клик_1_TB_SATA3_3_5': {'func': self.click_xpath, 'path': './/input[@class="server-storage-drive-item-checkbox ng-scope"]'},
    'Клик_login': {'func': self.click_xpath, 'path': './/div[@class="CurrentUserWidget-sc-1xtml1f-0 VMdDP"]'},
    'Клик_logout': {'func': self.click_xpath, 'path': './/span[text()="Logout"]'},
    'Swap_Free_of_charge': {'func': self.target, 'path': './/div[text()="Free of charge"]'},
    'Swap_Install_add_ons': {'func': self.target, 'path': './/span[text()="Install add-ons"]'},
    'Swap_hostname': {'func': self.target, 'path': './/div[@class="ng-binding server-hosts-selector-styles__name___sNI7S"]'},
    'Swap_email_login': {'func': self.target, 'path': './/div[@class="CurrentUserWidget-sc-1xtml1f-0 VMdDP"]'},
    'Button_Enter': {'func': self.click_xpath, 'path': './/input[@id="submit-login"]'},

        }
              #   MainPage
        self.xpath = self.pagex[name].get('path')  # выбор xpath по ключу
        self.func = self.pagex[name].get('func')  # имя функции из словаря
        self.func(self.xpath, index)  # Вызов нужной функции с ожиданием по xpath
        print('Шаг ' + step + '. Клик ' + name + ' произведен')

    def send_f(self, name, text, stap):
        step = str(stap)
        self.pages = {
            'Ввод_логина': {'func': self.send_name, 'path': 'email', 'text':text},
            'Ввод_пароля': {'func': self.send_name, 'path': 'pwd', 'text':text},
            'Ввод_hostname': {'func': self.send_name, 'path': 'hostname', 'text':text},
            'Send_login_paritet': {'func': self.send_name, 'path': 'Login', 'text':text},
            'Send_password_paritet': {'func': self.send_name, 'path': 'Password', 'text':text},

        }
        self.args = self.pages[name].get('path')  # выбор path по ключу
        self.func = self.pages[name].get('func')  # имя функции из словаря
        self.func(self.args, text)  # Вызов нужной функции с id = path
        print('Шаг ' + step + '.  ' + name + ' ' + text + ' произведен')




    def click_id(self, args):
        dep = args['path']
        self.waitForIDClickable(dep, 30)
        self.driver.find_element_by_id(dep).click()
        print('Клик', dep)

    def click_name(self, name, index):
        self.waitForNameVisible(name, 7)
        self.driver.find_element_by_id(name).click()
        # print('Клик', dep)

    def click_xpath(self, xpath, index):
        self.waitForElementClickable(xpath, 12)
        self.driver.find_elements_by_xpath(xpath)[index].click()

    def click_css(self, args):
        css = args['path']
        # print('css = ', css)
        # self.waitForElementClickable(css, 30)
        self.driver.find_element_by_css_selector(css).click()

    def target(self, xpath, index=0):
        self.waitForElementVisible(xpath, 5)
        target = self.driver.find_elements_by_xpath(xpath)[index]
        target.location_once_scrolled_into_view  # скролл до элемента target
        print('скролл до элемента target')

    # Проверка видимости элемента                                         #Exception
    def tester_vis_xpath(self, xpath):
        self.waitForElementVisible(xpath, 5)
        self.driver.find_element_by_xpath(xpath)
        # print('Клик', dep)

    # Проверка кликабельности элемента
    def tester_click_xpath(self, xpath):
        self.waitForElementClickable(xpath, 25)
        self.driver.find_element_by_xpath(xpath)
        # print('Клик', dep)

    def click_enter(self):
        self.click_xpath('.//button[@class="header__login"]')

    def waitForElementPresent(self, xpath, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def waitForElementClickable(self, xpath, timer):
        WebDriverWait(self.driver, timer).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def waitForElementVisible(self, xpath, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def waitForNameVisible(self, name, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.NAME, name)))

    def waitForIDVisible(self, id, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.ID, id)))

    def waitForIDClickable(self, id, timer):
        WebDriverWait(self.driver, timer).until(EC.element_to_be_clickable((By.ID, id)))

    #                                                OPERATIONS

    # Функция ввода
    def send_id(self, args):
        d_id = args['path']
        txt = args['text']
        # self.loger_info('path = ' + d_id + ', text = ' + txt)
        self.waitForIDVisible(d_id, 30)
        self.driver.find_element_by_id(d_id).send_keys(txt)
        return

    def send_name(self, name, txt):
        # print('path = ' + d_id + ', text = ' + txt)
        self.waitForNameVisible(name, 12)
        self.driver.find_element_by_name(name).send_keys(txt)

    def send_css(self, args):
        d_name = args['path']
        txt = args['text']
        self.driver.find_element_by_css_selector(d_name).send_keys(txt)
        return

    # Функция ввода
    def input(self, dclass, data):
        li_xpath = ('.//input[@class="%s"]' % dclass)
        # self.waitForElementClickable(li_xpath, 80)
        time.sleep(1)
        self.driver.find_element_by_xpath(li_xpath).send_keys(data)

    def login_servers_com(self, email, passw):
        self.send_f('Ввод_логина', email, 1)
        self.send_f('Ввод_пароля', passw, 2)
        self.click_f('Клик_Вход_Signin', 3)

    def login_paritet(self, email, passw):
        self.send_f('Send_login_paritet', email, 1)
        self.send_f('Send_password_paritet', passw, 2)
        self.click_f('Button_Enter', 3)

    def logout(self):
        self.click_f('Клик_login', 1)
        self.click_f('Клик_logout', 2)



