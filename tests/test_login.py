
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from curl import Test_url
from helpers import login_and_password_generator
import time

# Тесты на вход.
class Test_login():
    # Вход по кнопке "Войти в аккаует" на главной форме.
    def test_login_main_form(self, driver, registration):
        reg_data = registration.copy()
        Email = reg_data["login"]
        Password = reg_data["password"]
        # Ожидаем, что перешли на форму входа.
        time.sleep(10)
        # 1. Ждём кликабельности элемента
        email_field = WebDriverWait(driver, 50).until(EC.element_to_be_clickable(Locators.EMAIL_LOCATOR))
        # 2. Очищаем поле (на всякий случай)
        email_field.clear()
        # 3. Вводим текст
        email_field.send_keys(Email)
        # 4. Дополнительно: проверяем, что текст появился (опционально)
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_value(Locators.EMAIL_LOCATOR, Email))
        driver.find_element(*Locators.PASSWORD_LOCATOR).send_keys(Password)
       
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_ENTER)).click()
        #Ожидаем переход на главную форму.
        #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        WebDriverWait(driver, 10).until(EC.url_to_be(Test_url.main_site))
        assert driver.current_url == Test_url.main_site, (
                                "Ошибка перехода на главную страницу после логина."
                                                                )
            
    # Вход через кнопку "Личный кабинет".
    def test_login_through_the_personal_account_button(self, driver, registration):
        reg_data = registration.copy()
        Email = reg_data["login"]
        Password = reg_data["password"]
        #driver.find_element(*Locators.LOGIN_BUTTON_LOCATOR).click() # Нажимаем кнопку "Личный кабинет".
        time.sleep(2)
        # Заполняем форму входа в аккаунт.
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(Email)
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(Password)
        driver.find_element(*Locators.LOGIN_ENTER).click()
        # Ожидаем переход на главную форму.
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Test_url.main_site))
        assert driver.current_url == Test_url.main_site, (
                                "Ошибка перехода на главную страницу после логина."
                                                                )
      
    # Вход через кнопку в форме регистрации.
    def test_login_via_the_button_in_the_registration_form(self, driver, registration):
        login = registration["login"]
        password = registration["password"]
        #driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        time.sleep(2)
        # Ожидаем форму входа.
        
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Locators.BUTTON_IN_AFTER_REG))
         # Заполняем форму входа в аккаунт.
      
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login)
        
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(password)
        
        # Нажимаем кнопку войти в аккаунт.
        driver.find_element(*Locators.BUTTON_IN_AFTER_REG).click()
        # Ожидаем переход на главную форму.
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Test_url.main_site))
        assert driver.current_url == Test_url.main_site, (
                                "Ошибка перехода на главную страницу после логина."
                                                                ) 
             
    # Вход через кнопку в форме восстановления пароля.
    def test_login_through_the_button_in_the_password_recovery_form(self, driver, registration):
        login,  password = registration
        # Ожидаем форму входа.
       
        # Восстановить пароль.
       
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.RECOVER_THE_PASSWORD)).click()
        # Вспомнили пароль? Войти.
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_REM_PASS_IN)).click()
        time.sleep(2)
        # Заполняем форму входа в аккаунт.
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login)
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(password)
        
        # Нажимаем кнопку войти в аккаунт.
        driver.find_element(*Locators.LOGIN_BUTTON_LOCATOR).click()
        # Ожидаем переход на главную форму.
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Test_url.main_site))
        assert driver.current_url == Test_url.main_site, (
                                "Ошибка перехода на главную страницу после логина.")
      