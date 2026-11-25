# Lab 15 – Handling Multiple Windows/Tabs

## 1. Introduction
In this lab, I learned how to handle multiple browser windows and tabs using Selenium WebDriver.

## 2. Software Used
- Ubuntu 24.04
- Python 3.12.3
- Google Chrome 158.0.8127.88
- Selenium 4.25.0

## 3. Project Files
- `tabs.py` – Python Selenium script
- `index.html` – Main webpage
- `second.html` – Second webpage
- `requirements.txt` – Required Python package
- `evidence.txt` – Practical output
- `.gitignore` – Ignores temporary files

## 4. Python Virtual Environment
Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 5. Install Selenium
```bash
pip install selenium==4.25.0
```

## 6. Local Web Server
Start the local server:

```bash
python3 -m http.server 8000
```

Main webpage:

`http://localhost:8000/index.html`

## 7. Open a New Tab
The main page contains a link with `target="_blank"`.

Selenium clicks this link to open the second page in a new tab.

## 8. Get Window Handles
```python
window_handles = driver.window_handles
print(len(window_handles))
```

`driver.window_handles` returns all open browser window handles.

## 9. Switch Between Tabs
```python
driver.switch_to.window(handle)
```

This command switches the browser focus to the selected tab.

## 10. Extract Page Information
```python
print(driver.title)
print(driver.current_url)
```

- `driver.title` gets the page title.
- `driver.current_url` gets the current page URL.

## 11. Run the Practical
```bash
python tabs.py
```

## 12. Verified Output
```text
Opened: Main Page
Total open windows/tabs: 2
Title: Main Page
URL: http://localhost:8000/index.html
Title: Second Page
URL: http://localhost:8000/second.html
All multiple-window tests passed.
```

## 13. Browser Cleanup
```python
driver.quit()
```

This closes all browser windows opened by the WebDriver session.

## 14. Key Learnings
1. Open a new browser tab.
2. Get all window handles.
3. Switch between browser tabs.
4. Extract titles and URLs.
5. Verify results using assertions.
6. Close browser sessions properly.

## 15. Conclusion
Successfully completed the multiple-windows and tabs practical using Selenium WebDriver. Both browser tabs were opened, detected, switched, and verified.
