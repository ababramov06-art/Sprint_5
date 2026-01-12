
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from curl import Test_url
from helpers import login_and_password_generator

# Тесты на вход.
class Test_login():

    # Вход по кнопке "Войти в аккаует" на главной форме.
    def test_login_main_form(self, driver, registration):
        reg_data = registration.copy()
        Email = reg_data["login"]
        Password = reg_data["password"]
        # Ожидаем, что перешли на форму входа.
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.EMAIL_EDIT_LOGIN))
        time.sleep(3)
        # Заполняем форму входа в аккаунт.
        #driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(Email)
        #driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(Password)
        #driver.find_element(*Locators.LOGIN_ENTER).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.LOGIN_ENTER)).click()
        #Ожидаем переход на главную форму.
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        assert 'Оформить заказ'== element.text
            
    # Вход через кнопку "Личный кабинет".
    def test_login_through_the_personal_account_button(self, driver, registration):
        login, password = registration
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Личный кабинет".
       
        # Заполняем форму входа в аккаунт.
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login)
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(password)
        driver.find_element(*Locators.LOGIN_ENTER).click()
        # Ожидаем переход на главную форму.
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        assert 'Оформить заказ'== element.text
      
    # Вход через кнопку в форме регистрации.
    def test_login_via_the_button_in_the_registration_form(self, driver, registration):
        login = registration[login]
        password = registration[password]
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        
        # Ожидаем форму входа.
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_IN_AFTER_REG))
         # Заполняем форму входа в аккаунт.
      
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login)
        
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(password)
        
        # Нажимаем кнопку войти в аккаунт.
        driver.find_element(*Locators.BUTTON_IN_AFTER_REG).click()
        # Ожидаем переход на главную форму.
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        assert "Оформить заказ"== element.text
      
    # Вход через кнопку в форме восстановления пароля.
    def test_login_through_the_button_in_the_password_recovery_form(self, driver, registration):
        login,  password = registration
        # Зарегистрироваться.
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
       
        # Ожидаем форму входа.
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_IN_AFTER_REG))
        # Войти в аккаунт.
        driver.find_element(*Locators.BUTTON_IN_AFTER_REG).click()
        # Восстановить пароль.
        wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.RECOVER_THE_PASSWORD)).click()
        # Вспомнили пароль? Войти.
        wait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_REM_PASS_IN)).click()
        
        # Заполняем форму входа в аккаунт.
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login)
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(password)
        
        # Нажимаем кнопку войти в аккаунт.
        driver.find_element(*Locators.BUTTON_IN_AFTER_REG).click()
        # Ожидаем переход на главную форму.
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        assert "Оформить заказ"== element.text
      