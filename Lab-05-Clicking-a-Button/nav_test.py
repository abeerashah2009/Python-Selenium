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
    driver.get(Path("nav.html").resolve().as_uri())

    driver.find_element(By.ID, "goButton").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("next.html")
    )

    assert driver.title == "Next Page"
    print("URL:", driver.current_url)
    print("PASS: Button navigation verified.")

except Exception as e:
    print("FAIL:", e)
    sys.exit(1)

finally:
    driver.quit()
