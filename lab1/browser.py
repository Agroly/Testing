from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

# Инициализация драйвера Firefox
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 2. Ввести логин и пароль
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 3. Нажать кнопку Login
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # 4. Проверить успешный вход (наличие элемента "inventory_container")
    success = driver.find_element(By.ID, "inventory_container")
    if success.is_displayed():
        print("✅ Тест пройден: вход выполнен успешно!")
    else:
        print("❌ Тест не пройден: элемент не найден.")

except Exception as e:
    print("Ошибка во время теста:", e)

finally:
    time.sleep(3)
    driver.quit()
