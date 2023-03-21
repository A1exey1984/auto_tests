from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.XPATH, '//*[@id="treasure"]')
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x.get_attribute('valuex')))
    checkbox1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox1.click()
    radiobutton1 = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radiobutton1.click()
    button1 = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button1.click()

finally:
    time.sleep(5)
    browser.quit()
