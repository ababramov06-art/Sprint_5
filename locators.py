from selenium.webdriver.common.by import By
#заголовок страницы

# Логотип главной формы.
FORM_LOGO = (By.XPATH, "")

# Кнопка зарегистрироваться на форме входа в аккаунт.
BUTTON_REG = (By.XPATH, "//a[text()='Зарегистрироваться']")         

# Поле редактирования имени на форме регистрации.
NAME_EDIT = (By.XPATH, "//form[contains(@action, 'register')]//fieldset//div[contains(@class, 'input-group')")

# Поле редактирования почтового адреса на форме регистрации.
EMAIL_EDIT = (By.XPATH, "//form[contains(@action, 'register')]//input[@type='email' or contains(@placeholder, 'email')]")

# Поле редактирования пароля на форме регистрации.
PASSWORD_EDIT = (By.XPATH, "//form[contains(@action, 'register')]//div["
    "  contains(@class, 'input-group') or contains(@class, 'form-field')"
    "]") 

# Кнопка зарегистрироваться на форме регистрации.
BUTTON_REGISTER = (By.XPATH, "//form[contains(@action, 'register')]//button["
    "  contains(@class, 'submit') or text()='Отправить'"
    "]")    
