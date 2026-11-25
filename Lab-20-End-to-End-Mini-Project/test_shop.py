from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1280,800")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("http://127.0.0.1:8000/")
    print("Loaded:", driver.title)

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Dress")

    driver.find_element(By.NAME, "submit_search").click()

    alert = wait.until(EC.alert_is_present())
    assert "Dress" in alert.text, f"Unexpected alert: {alert.text}"
    print("Alert text:", alert.text)
    alert.accept()

    success_message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    assert "Success" in success_message.text
    print("Success message:", success_message.text)

    driver.save_screenshot("screenshot.png")
    assert "Search Results" in driver.title
    print("Updated title:", driver.title)

    print("All assertions passed.")

finally:
    driver.quit()
