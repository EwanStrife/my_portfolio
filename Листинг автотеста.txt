from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import string
import random
import time

driver = webdriver.Chrome(service=Service(executable_path="C:/Users/ibatu/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"))
print("TC2: Вход с валидными учетными данными")

try:
    driver.get("https://idemo.bspb.ru/")
    print("Успешно вошли на сайт")
    driver.maximize_window()
    print("Развернули окно браузера на весь экран")
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.clear()
    username.send_keys("demo")
    print("Ввели логин")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.clear()
    password.send_keys("demo")
    print("Ввели пароль")
    driver.find_element(By.ID, "login-button").click()
    print("Прошли двухфакторную аутентификацию")
    driver.find_element(By.ID, "login-otp-button").click()
    print("Успешно авторизовались")

    driver.find_element(By.XPATH, "//*[@id='cards-overview-index']").click()
    print("Перешли во вкладку карты")

    if driver.find_element(By.ID, "accounts-index"): print("\033[92m{}\033[0m".format("Test PASS"))
    driver.save_screenshot("scrshot_TC1.png")

except:
    driver.save_screenshot("error_TC1.png")
    print("\033[31m{}\033[0m".format("Test FAIL"))

    driver.quit()