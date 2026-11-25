# Lab 14 – Handling Alerts

## 1. Objective

Learn how to handle JavaScript alert and confirmation pop-ups using Selenium WebDriver and Python.

## 2. Environment

- Operating System: Ubuntu 24.04
- Python: 3.12
- Google Chrome: 158.0.8127.88
- Selenium: 4.25.0
- Browser mode: Headless

## 3. Project Files

- `alerts.py` – Selenium automation script
- `requirements.txt` – Python dependency
- `evidence.txt` – Practical test results
- `.gitignore` – Excludes virtual environment and Python cache files

## 4. Install Dependencies

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Selenium:

```bash
pip install -r requirements.txt
```

## 5. Test Website

The practical uses:

http://the-internet.herokuapp.com/javascript_alerts

Check website availability:

```bash
curl -s -o /dev/null -w "%{http_code}\n" \
http://the-internet.herokuapp.com/javascript_alerts
```

Expected HTTP status: `200`.

## 6. WebDriver Configuration

The script uses Chrome in headless mode:

- `--headless=new` runs Chrome without a display.
- `--no-sandbox` supports the lab server environment.
- `--disable-dev-shm-usage` avoids shared-memory issues.

Selenium Manager handles ChromeDriver setup.

## 7. Accepting a JavaScript Alert

The script:
1. Finds the JavaScript alert button using XPath.
2. Clicks the button.
3. Switches to the alert using `driver.switch_to.alert`.
4. Extracts the alert text using `alert.text`.
5. Checks the text using an assertion.
6. Accepts the alert using `alert.accept()`.

Expected alert text:

`I am a JS Alert`

Expected page result:

`You successfully clicked an alert`

## 8. Dismissing a Confirmation Dialog

The script:
1. Finds and clicks the JavaScript confirmation button.
2. Switches to the confirmation dialog.
3. Reads and verifies its text.
4. Dismisses the dialog using `confirm.dismiss()`.

Expected confirmation text:

`I am a JS Confirm`

Expected page result:

`You clicked: Cancel`

## 9. Closing the Browser

The script uses a `finally` block:

```python
finally:
    driver.quit()
```

This ensures the browser is closed after the test, including when an error occurs inside the `try` block.

## 10. Run the Practical

Check Python syntax:

```bash
python -m py_compile alerts.py
```

Run the Selenium script:

```bash
python alerts.py
```

## 11. Verified Output

```text
Page title: The Internet
Alert says: I am a JS Alert
Alert accepted successfully.
Result: You successfully clicked an alert
Confirm says: I am a JS Confirm
Result: You clicked: Cancel
All alert tests passed.
```

## 12. Browser Cleanup Verification

Command:

```bash
pgrep -a chrome || echo "no chrome processes"
```

Verified output:

```text
no chrome processes
```

## 13. Key Learnings

- Use `driver.switch_to.alert` to access JavaScript alerts.
- Use `alert.text` to extract alert messages.
- Use `alert.accept()` to accept an alert.
- Use `alert.dismiss()` to cancel a confirmation dialog.
- Use assertions to verify expected messages and page results.
- Use `driver.quit()` to close the browser safely.

## 14. Conclusion

Successfully completed the Handling Alerts practical using Python and Selenium WebDriver. Verified alert text extraction, accepting alerts, dismissing confirmation dialogs, page results, and browser cleanup.
