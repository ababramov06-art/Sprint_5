# Функция генерации уникальных логина и пароля.
def login_and_password_generator():
   
    # Использует UUID для уникальности.
    uid = str(uuid.uuid4().hex[:3])  # Короткие UUID
    login = f"37_Aleksandr_{uid}@yandex.ru"
    
    # Пароль: смесь букв, цифр и 2 спецсимвола
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=6))
    password += random.choice("!@#") + random.choice("$%&")
   
    return {"login": login, "password": password}