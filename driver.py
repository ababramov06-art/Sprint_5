import time
from locators import Locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(options)
driver.get('https://stellarburgers.education-services.ru/')

driver.find_element(*Locators.BUTTON_LOG_IN_TO_YOUR_ACCOUNT).click() # Нажимаем кнопку "Войти в аккаунт".
driver.find_element(*Locators.BUTTON_REG).click() # На форме входа нажимаем кнопку "Зарегистрироваться".

# Заполняем поля формы регистрации.
#driver.find_element(*Locators.NAME_EDIT).clear()
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('Aleksandr')
#driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('37_Aleksandr_1969@yandex.ru')
#driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input").send_keys('gfhjkm')
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

#driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/div/a/svg").click() # Жмём логотип формы. 

time.sleep(30)
driver.quit()