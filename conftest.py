import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 

@pytest.fixture(scope = "function")
def driver():
    options = Options()
    brouser = webdriver.Chrome(options)
    brouser.get("https://stellarburgers.education-services.ru/")
    yield brouser
    brouser.quit()

@pytest.fixture(scope = "session")
def login_and_password_generator():
    
    