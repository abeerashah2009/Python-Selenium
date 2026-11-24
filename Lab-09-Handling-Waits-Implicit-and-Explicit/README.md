# Lab 09: Handling Waits (Implicit and Explicit)

## 1. Objective
Learn how to handle delayed web elements in Selenium using implicit and explicit waits.

## 2. Tools Used
- Python 3
- Selenium 4.25.0
- Google Chrome
- Ubuntu Linux

## 3. Test HTML Page
Created `delayed.html` with JavaScript that adds a button after 3 seconds.

Button ID: `delayed-btn`

Initial button text: `Ready`

After clicking: `Clicked!`

## 4. Implicit Wait
Used:

```python
driver.implicitly_wait(5)
```

**Verified result:**
- Selenium found the delayed button.
- Element appeared after approximately 3 seconds.
- Button text: `Ready`

## 5. Short Implicit Wait Test
Changed the implicit wait to 1 second.

**Verified result:**
- Selenium raised `NoSuchElementException`.
- This was the expected result because the button appeared after 3 seconds.

## 6. Explicit Wait
Used:

```python
wait = WebDriverWait(driver, 10)
element = wait.until(
    EC.element_to_be_clickable((By.ID, 'delayed-btn'))
)
```

**Verified result:**
- Button became clickable after approximately 3.4 seconds.
- Before click: `Ready`
- After click: `Clicked!`

## 7. Browser Cleanup
Used `driver.quit()` in the `finally` block.

Verified that no Chrome processes remained after testing.

## 8. Key Learning
- Implicit wait sets a general timeout for element searches.
- Explicit wait waits for a specific condition.
- `NoSuchElementException` occurs when an element cannot be found within the configured wait.
- `element_to_be_clickable()` checks whether an element is visible and enabled.

## 9. Files
- `delayed.html` — Test page
- `implicit_wait.py` — 5-second implicit wait
- `implicit_short.py` — 1-second negative test
- `explicit_wait.py` — Explicit wait and button click
- `notes.txt` — Practical observations
