import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    driver.get('file://' + os.path.abspath('delayed.html'))

    start = time.time()
    wait = WebDriverWait(driver, 10)

    element = wait.until(
        EC.element_to_be_clickable((By.ID, 'delayed-btn'))
    )

    print('Clickable after about %.1f seconds' % (time.time() - start))
    print('Before click:', element.text)

    element.click()

    print('After click:', element.text)

finally:
    driver.quit()
