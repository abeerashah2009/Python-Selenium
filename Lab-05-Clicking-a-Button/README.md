# Lab 05 - Clicking a Button with Selenium

## 1. Lab Objective

Learn how to locate and click HTML buttons using Selenium WebDriver.

This lab covers:
- Finding buttons using element IDs
- Clicking buttons with Selenium
- Verifying changes on a webpage
- Testing navigation between pages
- Running Firefox in headless mode

## 2. Environment

- Operating System: Ubuntu 24.04 LTS
- Python: 3.12.3
- Selenium: 4.25.0
- Browser: Mozilla Firefox 160.0.1
- Browser Driver: Geckodriver (managed by Selenium Manager)

## 3. Project Files

| File | Purpose |
|---|---|
| sample.html | Sample page containing a button |
| click_test.py | Locates and clicks the sample button |
| nav.html | Page containing a navigation button |
| next.html | Destination page |
| nav_test.py | Tests button navigation |

## 4. Task 1 - Create a Sample Button

Created an HTML button with the ID `sampleButton`.

JavaScript uses:

```javascript
document.getElementById('sampleButton');
```

The button displays the text `Click Me!`.

## 5. Task 2 - Click a Button Using Selenium

Selenium locates the button:

```python
button = driver.find_element(By.ID, "sampleButton")
```

Click the button:

```python
button.click()
```

Wait for the result:

```python
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "result"))
)
```

The test verifies that `Button clicked!` appears on the webpage.

**Result:** PASS

## 6. Task 3 - Test Button Navigation

Created a navigation button in `nav.html`.

The button opens `next.html`.

Selenium clicks the button and waits for the URL to contain `next.html`.

The test verifies the destination page title:

```python
assert driver.title == "Next Page"
```

**Result:** PASS

## 7. Run the Tests

Activate the virtual environment and run:

```bash
source ~/button-lab/venv/bin/activate

python ~/button-lab/click_test.py
python ~/button-lab/nav_test.py
```

## 8. Important Selenium Concepts

- `webdriver.Firefox()` - Starts Firefox WebDriver.
- `By.ID` - Locates an element using its HTML ID.
- `find_element()` - Finds a webpage element.
- `.click()` - Clicks an element.
- `WebDriverWait` - Waits for a specific condition.
- `assert` - Checks whether an expected condition is true.
- `driver.quit()` - Closes the browser session.
- `-headless` - Runs the browser without a graphical window.

## 9. Conclusion

Successfully completed button identification, button clicking, webpage content verification, and navigation testing using Python Selenium and Firefox.
