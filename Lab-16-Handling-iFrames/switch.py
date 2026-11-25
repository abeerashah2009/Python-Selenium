import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("file://" + os.path.abspath("main.html"))

    try:
        driver.find_element(By.ID, "submitButton")
        print("button found in main page")
    except NoSuchElementException:
        print("button NOT found in main page")

    driver.switch_to.frame("exampleFrame")

    button = driver.find_element(By.ID, "submitButton")
    print("button found in iframe:", button.text)

    assert button.text.strip() == "Submit"
    print("Task 2 passed")

finally:
    driver.quit()
