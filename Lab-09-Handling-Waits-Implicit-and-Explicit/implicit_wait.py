import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    driver.get('file://' + os.path.abspath('delayed.html'))
    driver.implicitly_wait(5)

    start = time.time()
    element = driver.find_element(By.ID, 'delayed-btn')

    print('Found element text:', element.text)
    print('Waited about %.1f seconds' % (time.time() - start))

finally:
    driver.quit()
