from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://the-internet.herokuapp.com/javascript_alerts")
    print("Page title:", driver.title)

    # Accept JavaScript alert and verify its text
    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Alert']"
    ).click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Alert says:", alert_text)
    assert alert_text == "I am a JS Alert"

    alert.accept()
    print("Alert accepted successfully.")

    result = driver.find_element(By.ID, "result").text
    print("Result:", result)
    assert result == "You successfully clicked an alert"

    # Dismiss JavaScript confirmation
    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Confirm']"
    ).click()

    confirm = driver.switch_to.alert
    print("Confirm says:", confirm.text)
    assert confirm.text == "I am a JS Confirm"

    confirm.dismiss()

    result = driver.find_element(By.ID, "result").text
    print("Result:", result)
    assert result == "You clicked: Cancel"

    print("All alert tests passed.")

finally:
    driver.quit()
