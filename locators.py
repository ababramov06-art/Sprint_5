from selenium.webdriver.common.by import By

class Locators:
#заголовок страницы

# Кнопка зарегистрироваться на форме регистрации.
    BUTTON_REGISTER = (By.XPATH, "//*[@id='root']/div/main/div/form/button")    

# Кнопка "Сделать заказ".
    BUTTON_IN_ORDER = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")

# Кнопка "Войти".
    BUTTON_ENTER = (By.XPATH, "//*[@id='root']/div/main/div/form/button")

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

# Флюорисцентная булка.
    ROLS = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[1]")  

# Соусы.
    SOUSES = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[2]")

# Начинки"
    TOPPINGS = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]")

# логотип Stellar Burgers в header
    LOGO_LOCATOR = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")
# Логотип главной формы.
    FORM_LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")

 # Локаторы полей ввода логина и пароля (подарок от наставника)
    EMAIL_LOCATOR = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    PASSWORD_LOCATOR = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    # поле ввода имени в форме регистрации
    NAME_LOCATOR = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")

    # Кнопка "Войти в аккаунт" на главной странице и "Войти" в ЛК
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "button_button_type_primary")]')

    # ссылка "Войти" на страницах регистрации и восстановления пароля
    LOGIN_LINK_LOCATOR = (By.XPATH, '//*[contains(@class, "Auth_link")]')

    # кнопка "Зарегистрироваться" в форме регистрации
    REGISTER_BUTTON_LOCATOR = (
        By.XPATH, '//*[contains(@class, "button_button_type_primary")]')

    # кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT_BUTTON_LOCATOR = (
        By.XPATH, "// *[contains(text(), 'Личный Кабинет')]")

    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON_LOCATOR = (By.XPATH, "// *[contains(text(), 'Конструктор')]")

    # кнопка "Выход" в ЛК
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(@class, 'Account_button')]")

    # логотип Stellar Burgers в header
    LOGO_LOCATOR = (By.XPATH,"//*[contains(@class, 'AppHeader_header__logo')]")

    # Локаторы для вкладок конструктора
    CONSTRUCTOR_TAB_BUN_LOCATOR = (By.XPATH, "*//span[contains(text(), 'Булки')]")
    CONSTRUCTOR_TAB_SAUCE_LOCATOR = (By.XPATH, "*//span[contains(text(), 'Соусы')]")
    CONSTRUCTOR_TAB_FILLING_LOCATOR = (By.XPATH, "*//span[contains(text(), 'Начинки')]")

    # Локаторы для активных вкладок
    ACTIVE_TAB_BUN_LOCATOR = (By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current__2BEPc') "
        "and span/text()='Булки']")
    ACTIVE_TAB_SAUCE_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current__2BEPc') "
        "and span/text()='Соусы']")
    ACTIVE_TAB_FILLING_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current__2BEPc') "
        "and span/text()='Начинки']")

    # Локатор ошибки неправильного логина при регистрации
    ERROR_MESSAGE_LOCATOR = (
        By.CSS_SELECTOR,
        ".input__error.text_type_main-default")

    WRONG_PASS_MESSAGE_LOCATOR = (
        By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
