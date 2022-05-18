from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.implicitly_wait(5)

browser.get("https://www.pexels.com/search/aesthetic%20wallpaper/")

images = browser.find_elements(By.XPATH, "//a[@class='Link_link__mTUkz spacing_noMargin__Q_PsJ']//img")

file1 = open(f'data/image_links.txt', 'a')
for image in images:
    file1.write(image.get_attribute('src') + '\n')
file1.close()

browser.close()