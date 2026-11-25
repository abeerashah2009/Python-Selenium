from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Open the main page
    driver.get("http://localhost:8000/index.html")
    print("Opened:", driver.title)

    # Open the second page in a new tab
    link = driver.find_element(By.LINK_TEXT, "Open in a new tab")
    link.click()

    # Wait until the second tab opens
    WebDriverWait(driver, 10).until(
        EC.number_of_windows_to_be(2)
    )

    # List all open window handles
    window_handles = driver.window_handles
    print("Total open windows/tabs:", len(window_handles))
    assert len(window_handles) == 2

    # Switch between tabs and extract information
    for handle in window_handles:
        driver.switch_to.window(handle)

        print("Switched to handle:", handle)
        print("Title:", driver.title)
        print("URL:", driver.current_url)

    # Verify both pages
    titles = []

    for handle in window_handles:
        driver.switch_to.window(handle)
        titles.append(driver.title)

    assert "Main Page" in titles
    assert "Second Page" in titles

    print("All multiple-window tests passed.")

finally:
    driver.quit()
