from locators import Locators
from curl import Test_url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers import login_and_password_generator
import time

class Test_switching_from_our_personal_account_to_the_constructor():
    
    def test_switching_from_your_personal_account_click_to_the_constructor(self, driver):
        login = login_and_password_generator()["login"]
        password = login_and_password_generator()["password"]
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".
        # Заполняем поля формы регистрации.
        driver.find_element(*Locators.NAME_EDIT).clear()
        driver.find_element(*Locators.NAME_EDIT).send_keys('Aleksandr')

        driver.find_element(*Locators.EMAIL_EDIT).clear()
        driver.find_element(*Locators.EMAIL_EDIT).send_keys(login)

        driver.find_element(*Locators.PASSWORD_EDIT).clear()
        driver.find_element(*Locators.PASSWORD_EDIT).send_keys(password)
        
        # Нажимаем кнопку "Зарегистрироваться."
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # Ожидаем, что перешли на форму входа.
        time.sleep(1)
        # Заполняем форму входа в аккаунт.
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login)
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(password)
        driver.find_element(*Locators.LOGIN_ENTER).click()
       
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_CONSTR)).click()
        except_url = Test_url.main_site
        current_url = driver.current_url
        assert except_url == current_url
    
    def test_switching_from_your_personal_account_click_to_logo_Stellar_Burgers(self, driver):
        login = login_and_password_generator()["login"]
        password = login_and_password_generator()["password"]
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".
        # Заполняем поля формы регистрации.
        driver.find_element(*Locators.NAME_EDIT).clear()
        driver.find_element(*Locators.NAME_EDIT).send_keys('Aleksandr')

        driver.find_element(*Locators.EMAIL_EDIT).clear()
        driver.find_element(*Locators.EMAIL_EDIT).send_keys(login)

        driver.find_element(*Locators.PASSWORD_EDIT).clear()
        driver.find_element(*Locators.PASSWORD_EDIT).send_keys(password)
        
        # Нажимаем кнопку "Зарегистрироваться."
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # Ожидаем, что перешли на форму входа.
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_IN_AFTER_REG)).click()
        # Жмём логотип формы.
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.FORM_LOGO)).click()              
        # Ожидаем переход на главную форму.
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        
        except_url = Test_url.main_site
        current_url = driver.current_url
        assert except_url == current_url