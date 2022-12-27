import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox(executable_path="/Users/nikita_nik/Desktop/Firefoxtest/geckodriver")
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru')
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, "h1")))
   # Проверяем, что мы оказались на странице Авторизации
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
   yield

   pytest.driver.quit()

# Авторизация пользователя по номеру телефона с валидным номером телефона
def test_authorization_valid_number():
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("799999999999")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   #Проверяем url после редиректа
   assert pytest.driver.current_url == "https://b2c.passport.rt.ru/redirect_uri/"

# Авторизация пользователя по номеру телефона с невалидными номером телефона
def test_authorization_invalid_number():
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("799999999998")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "form-error-message")))

   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Авторизация пользователя по электронной почте с валидной электронной почтой
def test_authorization_valid_email():
   # Кликаем на таб "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("testvalid@mail.ru")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем url после редиректа
   assert pytest.driver.current_url == "https://b2c.passport.rt.ru/redirect_uri/"

# Авторизация пользователя по электронной почте с невалидной электронной почтой
def test_authorization_invalid_email():
   # Кликаем на таб "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("testinvalid@mail.ru")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "form-error-message")))

   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Авторизация пользователя по логину с валидным логином
def test_authorization_valid_login():
   # Кликаем на таб "Логин"
   pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("TestLogin")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем url после редиректа
   assert pytest.driver.current_url == "https://b2c.passport.rt.ru/redirect_uri/"

# Авторизация пользователя по логину с невалидным логином
def test_authorization_invalid_login():
   # Кликаем на таб "Логин"
   pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("LoginLog")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "form-error-message")))

   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Авторизация пользователя по лицевому счету с валидным лицевым счетом
def test_authorization_valid_ls():
   # Кликаем на таб "Лицевой счёт"
   pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("422524245425")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем url после редиректа
   assert pytest.driver.current_url == "https://b2c.passport.rt.ru/redirect_uri/"

# Авторизация пользователя по лицевому счету с невалидным лицевым счетом
def test_authorization_invalid_ls():
   # Кликаем на таб "Лицевой счёт"
   pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("422524245555")
   # Вводим пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh")
   # Нажимаем кнопку "Войти"
   login = pytest.driver.find_element(By.ID, 'kc-login').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "form-error-message")))

   assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

# Проверка переключения таба при вводе текста в поле  ”Номер телефона”
def test_authorization_tab():
   # Вводим номер телефона
   number = pytest.driver.find_element(By.ID, 'username').send_keys("testtest")
   password = pytest.driver.find_element(By.ID, 'password').click()

   element = WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".tabs-input-container__login > div:nth-child(1) > span:nth-child(4)")))

   assert pytest.driver.find_element(By.CSS_SELECTOR, '.tabs-input-container__login > div:nth-child(1) > span:nth-child(4)').text == "Логин"

# Регистрация пользователя с паролем менее 8 символов
def test_registration_password_less():
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.execute_script("arguments[0].scrollIntoView();", pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register'))
   pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register').click()
   pytest.driver.implicitly_wait(5)
   # Вводим Имя
   firstName = pytest.driver.find_element(By.NAME, 'firstName').send_keys("Алексей")
   # Вводим Фамилию
   lastName = pytest.driver.find_element(By.NAME, 'lastName').send_keys("Алексеев")
   # Вводим email
   email = pytest.driver.find_element(By.ID, 'address').send_keys("testtestow@mail.ru")
   # Вводим Пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQ")
   # Вводим подтверждение пароля
   password_confirm = pytest.driver.find_element(By.ID, 'password-confirm').send_keys("MyswWFQ")
   pytest.driver.find_element(By.NAME, 'lastName').click()
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(1) > span:nth-child(2)').text == "Длина пароля должна быть не менее 8 символов"
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(2) > span:nth-child(2)').text == "Длина пароля должна быть не менее 8 символов"

# Регистрация пользователя с паролем не содержащим заглавных букв
def test_registration_password_capital():
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.execute_script("arguments[0].scrollIntoView();", pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register'))
   pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register').click()
   pytest.driver.implicitly_wait(5)
   # Вводим Имя
   firstName = pytest.driver.find_element(By.NAME, 'firstName').send_keys("Алексей")
   # Вводим Фамилию
   lastName = pytest.driver.find_element(By.NAME, 'lastName').send_keys("Алексеев")
   # Вводим email
   email = pytest.driver.find_element(By.ID, 'address').send_keys("testtestow@mail.ru")
   # Вводим Пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("testtest1")
   # Вводим подтверждение пароля
   password_confirm = pytest.driver.find_element(By.ID, 'password-confirm').send_keys("testtest1")
   pytest.driver.find_element(By.NAME, 'lastName').click()
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(1) > span:nth-child(2)').text == "Пароль должен содержать хотя бы одну заглавную букву"
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(2) > span:nth-child(2)').text == "Пароль должен содержать хотя бы одну заглавную букву"

# Регистрация пользователя с паролем не содержащим латинских букв
def test_registration_password_eng():
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.execute_script("arguments[0].scrollIntoView();", pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register'))
   pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register').click()
   pytest.driver.implicitly_wait(5)
   # Вводим Имя
   firstName = pytest.driver.find_element(By.NAME, 'firstName').send_keys("Алексей")
   # Вводим Фамилию
   lastName = pytest.driver.find_element(By.NAME, 'lastName').send_keys("Алексеев")
   # Вводим email
   email = pytest.driver.find_element(By.ID, 'address').send_keys("testtestow@mail.ru")
   # Вводим Пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("тесттест")
   # Вводим подтверждение пароля
   password_confirm = pytest.driver.find_element(By.ID, 'password-confirm').send_keys("тесттест")
   pytest.driver.find_element(By.NAME, 'lastName').click()
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(1) > span:nth-child(2)').text == "Пароль должен содержать только латинские буквы"
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(2) > span:nth-child(2)').text == "Пароль должен содержать только латинские буквы"

# Регистрация пользователя с разными паролями в полях “Пароль” и “Подтвердите пароль”
def test_registration_password_dublicat():
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.execute_script("arguments[0].scrollIntoView();", pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register'))
   pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register').click()
   pytest.driver.implicitly_wait(5)
   # Вводим Имя
   firstName = pytest.driver.find_element(By.NAME, 'firstName').send_keys("Алексей")
   # Вводим Фамилию
   lastName = pytest.driver.find_element(By.NAME, 'lastName').send_keys("Алексеев")
   # Вводим email
   email = pytest.driver.find_element(By.ID, 'address').send_keys("testtestow@mail.ru")
   # Вводим Пароль
   password = pytest.driver.find_element(By.ID, 'password').send_keys("MyswWFQh1")
   # Вводим подтверждение пароля
   password_confirm = pytest.driver.find_element(By.ID, 'password-confirm').send_keys("MyswWFQh12")
   button = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-btn').click()
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(2) > span:nth-child(2)').text == "Пароли не совпадают"

# Регистрация пользователя с пустыми полями “Пароль” и “Подтвердите пароль””
def test_registration_password_empty():
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.execute_script("arguments[0].scrollIntoView();", pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register'))
   pytest.driver.find_element(By.CSS_SELECTOR, '#kc-register').click()
   pytest.driver.implicitly_wait(5)
   # Вводим Имя
   firstName = pytest.driver.find_element(By.NAME, 'firstName').send_keys("Алексей")
   # Вводим Фамилию
   lastName = pytest.driver.find_element(By.NAME, 'lastName').send_keys("Алексеев")
   # Вводим email
   email = pytest.driver.find_element(By.ID, 'address').send_keys("testtestow@mail.ru")
   button = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-btn').click()
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(1) > span:nth-child(2)').text == "Длина пароля должна быть не менее 8 символов"
   assert pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container--error:nth-child(2) > span:nth-child(2)').text == "Длина пароля должна быть не менее 8 символов"

# Проверка кнопки “Вернуться назад”
def test_registration_password_restore():
   # Нажимаем на кнопку "Забыли пароль"
   pytest.driver.find_element(By.CSS_SELECTOR, '#forgot_password').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "reset-back")))

   pytest.driver.find_element(By.ID, 'reset-back').click()

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, "h1")))

   # Проверяем, что мы оказались на странице Авторизации
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"

