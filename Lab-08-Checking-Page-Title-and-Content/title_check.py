from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-headless")
options.set_preference("network.proxy.type", 0)
driver = webdriver.Firefox(options=options)

try:
    driver.get("http://127.0.0.1:8000/")

    page_title = driver.title
    print(f"Page Title: {page_title}")
    expected_title = "Welcome to Al-Nafi Lab"
    assert page_title == expected_title, f"Title mismatch! Expected: {expected_title}, but got: {page_title}"

    element = driver.find_element(By.XPATH, "//a[text()='Downloads']")
    actual_text = element.text
    expected_text = "Downloads"
    assert actual_text == expected_text, f"Text mismatch! Expected: {expected_text}, but got: {actual_text}"
    print(f"Link Text: {actual_text}")

finally:
    driver.quit()
