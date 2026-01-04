from selenium.webdriver.common.by import By

class Locators:
#заголовок страницы

# Логотип главной формы.
    FORM_LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div/a/svg")

# Кнопка "Сделать заказ".
    BUTTON_IN_ORDER = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")

# Кнопка "Конструктор".
    BUTTON_CONSTR = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")

# Кнопка "Войти в аккаунт" на клавной форме.
    BUTTON_LOG_IN_TO_YOUR_ACCOUNT = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")

# Кнопка зарегистрироваться на форме входа в аккаунт.
    BUTTON_REG = (By.XPATH, "//a[text()='Зарегистрироваться']")         

# Поле редактирования имени на форме регистрации.
    NAME_EDIT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")

# Поле редактирования почтового адреса на форме регистрации.
    EMAIL_EDIT =       (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    EMAIL_EDIT_LOGIN = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    
# Поле редактирования пароля на форме регистрации.
    PASSWORD_EDIT =       (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input") 
    PASSWORD_EDIT_LOGIN = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    
# Кнопка зарегистрироваться на форме регистрации.
    BUTTON_REGISTER = (By.XPATH, "//*[@id='root']/div/main/div/form/button")    

# Сообщение об ошибке пароля.
    WRONG_PASS_MESSAGE_LOCATOR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

# Кнопка "Личный кабинет."
    PERSONAL_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")

# Кнопка "Восстановить пароль" на странице входа.
    RECOVER_THE_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a")

# Кнопка "Логин" на странице восстановления пароля.
    LOGIN_IN_RECOVER = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a")

# Кнопка "Войти" на странице входа в аккаунт.
    LOGIN_ENTER = (By.XPATH, "//*[@id='root']/div/main/div/form/button")
                            
# Кнопка "Оформить заказ" на главной форме.
    PLACE_AN_ORDER = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")

# Кнопка "Войти" после регистрации.
    BUTTON_IN_AFTER_REG = (By.XPATH, "//*[@id='root']/div/main/div/form/button")

# Кнопка "Личный кабинет".
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")

# Надпись в личном кабинете.
    LABLE_PERSONAL_ACCOUNT = (By.XPATH, "//*[@id='root']/div/main/div/nav/p")

# Кнопка "Выход" личного кабинета.
    BUTTON_OUT_PERSONAL_ACCOUNT = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")

# Кнопка "Вспомнили пароль? Войти"
    BUTTON_REM_PASS_IN = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a")