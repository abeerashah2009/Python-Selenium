# Lab 11 – Locating Multiple Elements with Selenium

## 1. Lab Objective

The objective of this lab is to locate multiple HTML elements on a webpage using Selenium WebDriver.

In this lab, I created a local HTML page containing four hyperlinks and used Selenium to find and display their text and URLs.

## 2. Tools and Technologies

- Operating System: Ubuntu 24.04
- Programming Language: Python 3.12
- Automation Tool: Selenium 4.25.0
- Browser: Google Chrome 158
- HTML

## 3. Create the HTML Page

Created `links.html` containing four hyperlinks:

- Example
- Python
- Selenium
- Ubuntu

The page also contains a paragraph that is not a hyperlink.

## 4. Python Selenium Script

Created `links.py` to automate the browser.

The script performs these operations:

1. Imports Selenium libraries.
2. Configures Chrome in headless mode.
3. Opens the local HTML page.
4. Reads the page title.
5. Locates all hyperlinks using `find_elements()`.
6. Displays each link's visible text and URL.
7. Displays the total number of links.
8. Closes the browser using `driver.quit()`.

## 5. Locating Multiple Elements

Used the following Selenium command:

```python
links = driver.find_elements(By.TAG_NAME, "a")
```

`find_elements()` returns all matching elements as a list.

The `By.TAG_NAME` locator searches for HTML elements using their tag name.

The `a` tag represents an HTML hyperlink.

## 6. Display Link Information

Used a loop to display each hyperlink:

```python
for link in links:
    print(link.text, link.get_attribute("href"))
```

- `link.text` retrieves the visible link text.
- `get_attribute("href")` retrieves the link URL.

## 7. Verification Results

The Selenium script successfully displayed:

```text
Page title: Links Lab
Example https://example.com/
Python https://www.python.org/
Selenium https://www.selenium.dev/
Ubuntu https://ubuntu.com/
Total number of links found: 4
```

The HTML page contains four hyperlinks, and Selenium successfully located all four.

## 8. Python Syntax Verification

Command:

```bash
python3 -m py_compile links.py
```

Result: Passed with no syntax errors.

## 9. Browser Cleanup

The script uses:

```python
finally:
    driver.quit()
```

This ensures that the browser session is closed after execution.

Verified that no Chrome processes remained after the test.

## 10. Key Learning Outcomes

- Understanding Selenium WebDriver.
- Opening local HTML pages.
- Using `find_elements()` to locate multiple elements.
- Locating elements by HTML tag name.
- Extracting visible text and hyperlink URLs.
- Iterating through WebElement lists.
- Counting matching elements.
- Closing browser sessions safely.

**Lab Status:** Practical execution and verification completed.
