from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators

from helpers import login_and_password_generator

from curl import Test_url

class TestRegistration:
    def test_successful_registration(self, driver):
        expected_url = Test_url.page_log_in_to_your_account
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
        #driver.find_element(*Locators.BUTTON_REGISTER).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.BUTTON_REGISTER)).click()
        # Ожидаем форму входа.
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(expected_url))
        current_url = driver.current_url
        assert expected_url == current_url
     
       

    def test_unsuccessful_registration(self, driver):
        login = login_and_password_generator()["login"]
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".
        # Заполняем поля формы регистрации.
        driver.find_element(*Locators.NAME_EDIT).clear()
        driver.find_element(*Locators.NAME_EDIT).send_keys('Aleksandr')

        driver.find_element(*Locators.EMAIL_EDIT).clear()
        driver.find_element(*Locators.EMAIL_EDIT).send_keys(login)

        driver.find_element(*Locators.PASSWORD_EDIT).clear()
        driver.find_element(*Locators.PASSWORD_EDIT).send_keys("123")
        
        # Нажимаем кнопку "Зарегистрироваться."
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.WRONG_PASS_MESSAGE_LOCATOR)).text

        assert 'Некорректный пароль' == error_message
   