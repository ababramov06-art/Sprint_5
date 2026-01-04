from locators import Locators
from curl import Test_url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Test_transfer_to_your_personal_account():
    
    def test_transfer_to_your_personal_account(self, driver, login_and_password_generator):
        mail, password = login_and_password_generator
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
        # Ожидаем, что перешли на форму входа.
        time.sleep(1)
        # Заполняем форму входа в аккаунт.
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).clear()
        driver.find_element(*Locators.EMAIL_EDIT_LOGIN).send_keys(login_and_password_generator["login"])
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).clear()
        driver.find_element(*Locators.PASSWORD_EDIT_LOGIN).send_keys(login_and_password_generator["password"])
        driver.find_element(*Locators.LOGIN_ENTER).click()
        # Ожидаем переход на главную форму.
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        time.sleep(3)        
        assert Test_url.page_personal_account == driver.current_url