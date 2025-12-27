import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 

@pytest.fixture(scope = "class")
def driver():
    options = Options()
    brouser = webdriver.Chrome(options)
    brouser.get("https://stellarburgers.education-services.ru/")
    yield brouser
    brouser.quit()
    