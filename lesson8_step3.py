from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x) + int(y))


browser = None
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.XPATH, '//*[@id="num1"]')
    y = browser.find_element(By.XPATH, '//*[@id="num2"]')
    x, y = x.text, y.text

    select = Select(browser.find_element(By.XPATH, "//*[@id='dropdown']"))
    select.select_by_value(f'{calc(x, y)}')

    button1 = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button1.click()

finally:
    time.sleep(5)
    browser.quit()
