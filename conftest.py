import pytest
import uuid
import random
import string
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from curl import Test_url
from locators import Locators
from helpers import login_and_password_generator

# Запускаем приложение в Chuome.
@pytest.fixture(scope = "session")
def driver():
    options = Options()
    brouser = webdriver.Chrome(options)
    brouser.get(Test_url.main_site)
    yield brouser
    brouser.quit()


@pytest.fixture(scope = "session")
def registration(driver):
    
    Name ='Aleksandr'
    reg_data = login_and_password_generator().copy()
    Email = reg_data["login"]
    Password = reg_data["password"]
    
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
    time.sleep(2)
    # Жмём кнопочку зарегистрироваться.
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable(Locators.BUTTON_REGISTER)).click()
    return {"login": Email, "password": Password}
    