from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = None
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x.text

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(calc(x))
    button1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button1.click()
finally:
    time.sleep(5)
    browser.quit()

