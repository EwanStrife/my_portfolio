from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import string
import random
import time

driver = webdriver.Chrome(service=Service(executable_path="C:/Users/ibatu/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"))
try:
    driver.get("https://guru.qahacking.ru/index.php/magazin")
    print("Вошли на страницу магазина")
    driver.find_element(By.XPATH, "//*[@id='comjshop_list_product']/div[1]/div[1]/div/div/div[3]/div[7]/a[1]").click()
    print("Переместили товар в корзину")

    if driver.find_element(By.XPATH, "//*[@id='comjshop']/form/table[1]/tbody/tr[2]/td[2]/div[2]/a"):
        print("Проверили наличие товара в корзине по его наименованию")
        print("\033[92m{}\033[0m".format("Test PASS"))
        driver.save_screenshot("screenshot_TC1_PASS.png")

except:
    print("Наименование товара отсутствует в корзине")
    print("\033[31m{}\033[0m".format("Test FAIL"))
    driver.save_screenshot("screenshot_TC1_FAIL.png")

    driver.quit()

