import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--window-size=1280,800")

driver = webdriver.Chrome(options=opts)

try:
    driver.get("http://localhost:8000/")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    timestamped_file = f"screenshot_{timestamp}.png"
    driver.save_screenshot(timestamped_file)
    print("Saved:", timestamped_file)
finally:
    driver.quit()
