import os
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("file://" + os.path.abspath("main.html"))

    driver.switch_to.frame(0)

    status = driver.find_element(By.ID, "status")
    print("before:", status.text)

    driver.find_element(By.ID, "submitButton").click()

    status = driver.find_element(By.ID, "status")
    print("after:", status.text)

    assert status.text == "clicked"
    print("Task 3 passed")

finally:
    driver.quit()
