from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.implicitly_wait(5)

browser.get("http://www.quotationspage.com/random.php")

caption = browser.find_elements(By.XPATH, "//dt[@class='quote']//a")

file1 = open(f'data/caption.txt', 'a')
for cap in caption:
    file1.write(cap.text + '\n')
file1.close()

browser.close()