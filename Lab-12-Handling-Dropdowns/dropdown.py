import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("file://" + os.path.abspath("dropdown.html"))

    dropdown = driver.find_element(By.ID, "dropdown-example")

    select_element = Select(dropdown)

    select_element.select_by_visible_text("Option 2")
    print("After text select:", select_element.first_selected_option.text)

    assert select_element.first_selected_option.text == "Option 2"

    select_element.select_by_value("3")

    selected_option = select_element.first_selected_option
    print("Selected option:", selected_option.text)

    assert selected_option.text == "Option 3"

finally:
    driver.quit()
