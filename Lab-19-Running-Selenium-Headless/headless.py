import argparse
import time
import psutil
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser()
parser.add_argument(
    "mode",
    choices=["headless", "headed"],
    help="Choose headless or headed browser mode"
)
args = parser.parse_args()

options = Options()

options.binary_location = str(
    Path.home() / ".cache/selenium/chrome/chrome-linux64/chrome"
)

if args.mode == "headless":
    options.add_argument("--headless=new")

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1280,800")

start_time = time.time()
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:8000")

    elapsed = time.time() - start_time

    print("Browser mode:", args.mode)
    print("Page title:", driver.title)
    print(f"Execution time: {elapsed:.2f} seconds")

    screenshot_file = f"shot-{args.mode}.png"
    driver.save_screenshot(screenshot_file)
    print("Screenshot saved:", screenshot_file)

    chrome_processes = []

    for process in psutil.process_iter(["name", "memory_info"]):
        try:
            name = process.info["name"] or ""
            if "chrome" in name.lower():
                chrome_processes.append(process.info["memory_info"].rss)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    total_memory = sum(chrome_processes) / (1024 * 1024)
    print("Chrome processes:", len(chrome_processes))
    print(f"Total Chrome RSS: {total_memory:.2f} MB")

finally:
    driver.quit()
