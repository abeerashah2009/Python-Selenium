import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.binary_location = "/usr/lib/firefox/firefox"
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

try:
    driver.get("http://localhost:5000/")

    file_input = driver.find_element(By.ID, "fileInput")
    file_input.send_keys(os.path.abspath("sample.txt"))
    print("Selected file:", file_input.get_attribute("value"))

    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

    WebDriverWait(driver, 10).until(
        lambda d: "Upload OK" in d.find_element(By.TAG_NAME, "body").text
    )

    body = driver.find_element(By.TAG_NAME, "body").text
    print("Page says:", body)
    print("Upload OK")

finally:
    driver.quit()
