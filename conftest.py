import pytest
import uuid
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from curl import Test_url
from locators import Locators
from helpers import login_and_password_generator

# Запускаем приложение в Chuome.
@pytest.fixture(scope = "function")
def driver():
    options = Options()
    brouser = webdriver.Chrome(options)
    brouser.get("https://stellarburgers.education-services.ru/")
    yield brouser
    brouser.quit()


@pytest.fixture(scope = "function")
def registration(driver, ):
    
    Name ='Aleksandr'
    Email, Password = login_and_password_generator()
    driver.get(Test_url.page_registration)
    # Заполняем поля на форме регистрации.
    # Поле редактирования имени на форме регистрации.
    driver.find_element(*Locators.NAME_EDIT).clear()
    driver.find_element(*Locators.NAME_EDIT).send_keys(Name)
    #Поле редактирования почтового адреса на форме регистрации.
    driver.find_element(*Locators.EMAIL_EDIT).clear()
    driver.find_element(*Locators.EMAIL_EDIT).send_keys(Email)
    # Поле редактирования пароля на форме регистрации.
    driver.find_element(*Locators.PASSWORD_EDIT).clear()
    driver.find_element(*Locators.PASSWORD_EDIT).send_keys(Password)

    # Жмём кнопочку зарегистрироваться.
    driver.find_element(*Locators.BUTTON_REGISTER).click()
    return {Email, Password}