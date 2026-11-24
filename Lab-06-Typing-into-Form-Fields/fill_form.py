from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:8000/form.html")

    input_field = driver.find_element(By.ID, "username")
    input_field.send_keys("testuser")
    assert input_field.get_attribute("value") == "testuser"

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("securepassword123")
    assert password_field.get_attribute("value") == "securepassword123"

    print("Username value:", input_field.get_attribute("value"))
    print("Password value:", password_field.get_attribute("value"))
    print("Username and password fields populated successfully.")

finally:
    driver.quit()
