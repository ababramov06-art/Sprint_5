import pytest
import uuid
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from curl import Test_url
from locators import Locators

# Запускаем приложение в Chuome.
@pytest.fixture(scope = "function")
def driver():
    options = Options()
    brouser = webdriver.Chrome(options)
    brouser.get("https://stellarburgers.education-services.ru/")
    yield brouser
    brouser.quit()

# Генерируем уникальные почту и пароль для регистрации.
@pytest.fixture(scope = "function")
def login_and_password_generator():
   
    # Использует UUID для уникальности.
    uid = str(uuid.uuid4().hex[:3])  # Короткие UUID
    login = f"37_Aleksandr_{uid}@yandex.ru"
    
    # Пароль: смесь букв, цифр и 2 спецсимвола
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=6))
    password += random.choice("!@#") + random.choice("$%&")
   
    return {"login": login, "password": password}

@pytest.fixture(scope = "function")
def registration(driver, login_and_password_generator):
    
    Name ='Aleksandr'
    Email, Password = login_and_password_generator
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
    driver.quit()
    return {Email, Password}