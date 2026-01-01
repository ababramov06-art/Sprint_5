
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from curl import Test_url
import time
# Тесты на вход.
class Test_login():

    # Вход по кнопке "Войти в аккаует" на главной форме.
    def test_login_main_form(self, driver, login_and_password_generator):
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
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(Locators.PLACE_AN_ORDER))
        assert 'Оформить заказ'== element.text
        driver.quit()
        
    # Вход через кнопку "Личный кабинет".
    def test_login_through_the_personal_account_button(self, driver, login_and_password_generator):
        assert 1==1

    # Вход через кнопку в форме регистрации.
    def test_login_via_the_button_in_the_registration_form(self, driver, login_and_password_generator):
        assert 1==1

    # Вход через кнопку в форме восстановления пароля.
    def test_login_through_the_button_in_the_password_recovery_form(self, driver, login_and_password_generator):
        assert 1==1
      