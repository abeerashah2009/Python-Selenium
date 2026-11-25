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

    frames = driver.find_elements(By.TAG_NAME, "iframe")

    print("iFrames found:", len(frames))

    for index, frame in enumerate(frames):
        print("Index:", index)
        print("ID:", frame.get_attribute("id"))
        print("Name:", frame.get_attribute("name"))

    assert len(frames) == 1
    print("Task 1 passed")

finally:
    driver.quit()
