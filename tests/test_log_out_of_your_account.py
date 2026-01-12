from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from curl import Test_url
from helpers import login_and_password_generator

class Test_log_out_of_your_account():
    # проверка выхода из личного аккаута.
    def test_log_out_of_your_account(self, driver):
        mail = login_and_password_generator()["login"]
        password = login_and_password_generator()["password"]
        
        driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
        driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".
        # Заполняем поля формы регистрации.
        driver.find_element(*Locators.NAME_EDIT).clear()
        driver.find_element(*Locators.NAME_EDIT).send_keys('Aleksandr')

        driver.find_element(*Locators.EMAIL_EDIT).clear()
        driver.find_element(*Locators.EMAIL_EDIT).send_keys(mail)

        driver.find_element(*Locators.PASSWORD_EDIT).clear()
        driver.find_element(*Locators.PASSWORD_EDIT).send_keys(password)
        # Нажимаем кнопку "Зарегистрироваться."
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # Ожидаем переход на главную форму.
        driver.get(Test_url.main_site)
        # войти в личный кабинет.
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        # Ожидаем форму личного кабинета.
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.BUTTON_REG))
        # Проверяем форму личного кабинета.
        current_url = driver.current_url
        expected_url = Test_url.page_log_in_to_your_account
        assert expected_url == current_url
       