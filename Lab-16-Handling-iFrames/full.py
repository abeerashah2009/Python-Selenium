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

    driver.switch_to.frame("exampleFrame")
    driver.find_element(By.ID, "submitButton").click()

    print("status in iframe:", driver.find_element(By.ID, "status").text)

    driver.switch_to.default_content()

    print("main title:", driver.find_element(By.ID, "title").text)

    try:
        driver.find_element(By.ID, "submitButton")
        print("button reachable from main (unexpected)")
        raise AssertionError("Button should not be reachable from main context")
    except NoSuchElementException:
        print("button not reachable from main (expected)")

    assert driver.find_element(By.ID, "title").text == "Main Page"
    print("Task 4 passed")

finally:
    driver.quit()
