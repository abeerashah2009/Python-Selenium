import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)

try:
    driver.get(Path("sample.html").resolve().as_uri())

    print("Title:", driver.title)

    button = driver.find_element(By.ID, "sampleButton")
    print("Button text:", button.text)
    print("Button tag:", button.tag_name)

    button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )

    assert "Button clicked!" in driver.page_source
    print("PASS: Button clicked and result verified.")

except Exception as e:
    print("FAIL:", e)
    sys.exit(1)

finally:
    driver.quit()
