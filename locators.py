from selenium.webdriver.common.by import By

class Locators:
#заголовок страницы

# Логотип главной формы.
    FORM_LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div/a/svg")

# Кнопка "Войти в аккаунт" на клавной форме.
    BUTTON_LOG_IN_TO_YOUR_ACCOUNT = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")

# Кнопка зарегистрироваться на форме входа в аккаунт.
    BUTTON_REG = (By.XPATH, "//a[text()='Зарегистрироваться']")         

# Поле редактирования имени на форме регистрации.
    NAME_EDIT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")

# Поле редактирования почтового адреса на форме регистрации.
    EMAIL_EDIT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")

# Поле редактирования пароля на форме регистрации.
    PASSWORD_EDIT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input") 

# Кнопка зарегистрироваться на форме регистрации.
    BUTTON_REGISTER = (By.XPATH, "//form[contains(@action, 'register')]//button["
        "  contains(@class, 'submit') or text()='Отправить'"
        "]")    
