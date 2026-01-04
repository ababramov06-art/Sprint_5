from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators
import time
from curl import Test_url

class TestRegistration:
    def test_successful_registration(self, driver, login_and_password_generator):
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".
        # Заполняем поля формы регистрации.
        driver.find_element(*Locators.NAME_EDIT).clear()
        driver.find_element(*Locators.NAME_EDIT).send_keys('Aleksandr')

        driver.find_element(*Locators.EMAIL_EDIT).clear()
        driver.find_element(*Locators.EMAIL_EDIT).send_keys(login_and_password_generator["login"])

        driver.find_element(*Locators.PASSWORD_EDIT).clear()
        driver.find_element(*Locators.PASSWORD_EDIT).send_keys(login_and_password_generator["password"])
        
        # Нажимаем кнопку "Зарегистрироваться."
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # Ожидаем форму входа.
        time.sleep(5)
        current_url = driver.current_url
        expected_url = Test_url.page_LOG_IN_TO_YOUR_ACCOUNT

        assert expected_url == current_url
        driver.quit()
       

    def test_unsuccessful_registration(self, driver, login_and_password_generator):
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".
        # Заполняем поля формы регистрации.
        driver.find_element(*Locators.NAME_EDIT).clear()
        driver.find_element(*Locators.NAME_EDIT).send_keys('Aleksandr')

        driver.find_element(*Locators.EMAIL_EDIT).clear()
        driver.find_element(*Locators.EMAIL_EDIT).send_keys(login_and_password_generator["login"])

        driver.find_element(*Locators.PASSWORD_EDIT).clear()
        driver.find_element(*Locators.PASSWORD_EDIT).send_keys("123")
        
        # Нажимаем кнопку "Зарегистрироваться."
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.WRONG_PASS_MESSAGE_LOCATOR)).text

        assert 'Некорректный пароль' == error_message
        driver.quit()