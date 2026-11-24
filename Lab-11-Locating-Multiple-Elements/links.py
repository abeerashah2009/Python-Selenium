from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    driver.get(Path("links.html").resolve().as_uri())
    print("Page title:", driver.title)

    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        print(link.text, link.get_attribute("href"))

    print(f"Total number of links found: {len(links)}")

finally:
    driver.quit()
