# Lab 06 - Typing into Form Fields (send_keys)

## 1. Lab Objective

The objective of this lab is to learn how to enter text into web form fields using Selenium's `send_keys()` method.

## 2. Tools and Technologies

- Python 3
- Selenium 4.25.0
- Google Chrome
- ChromeDriver
- Ubuntu Linux
- HTML

## 3. Project Files

- `form.html` - A local HTML page containing username and password fields.
- `fill_form.py` - A Selenium script that locates the form fields and enters text.
- `README.md` - Lab notes and documentation.
- `evidence.txt` - Practical verification notes.

## 4. HTML Form

The HTML page contains two input fields:

- Username field with ID `username`
- Password field with ID `password`

## 5. Selenium Imports

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
```

These imports provide browser automation, element location, and Chrome configuration.

## 6. Chrome Configuration

```python
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
```

These options configure Chrome to run in headless mode.

## 7. Locating Form Fields

```python
input_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
```

`find_element()` locates HTML elements using their IDs.

## 8. Using send_keys()

```python
input_field.send_keys("testuser")
password_field.send_keys("securepassword123")
```

The `send_keys()` method types text into the selected input fields.

## 9. Verification

The script uses assertions to verify that both fields contain the expected values.

```python
assert input_field.get_attribute("value") == "testuser"
assert password_field.get_attribute("value") == "securepassword123"
```

## 10. Browser Cleanup

```python
finally:
    driver.quit()
```

`driver.quit()` closes the browser session after execution.

## 11. Important Learning Points

1. How to locate HTML elements using `By.ID`.
2. How to enter text using `send_keys()`.
3. How to read input values using `get_attribute("value")`.
4. How to verify results using assertions.
5. How to configure and close a headless Chrome browser.

## 12. Conclusion

This lab demonstrates how Selenium automates typing into username and password fields on a local HTML form. It introduces a basic technique used in automated web form testing.
