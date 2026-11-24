# Lab 10 - Taking Screenshots with Selenium

## 1. Lab Objective
Learn how to capture screenshots of a webpage using Selenium WebDriver and Python.

## 2. Tools and Technologies
- Ubuntu 24.04
- Python 3.12
- Selenium 4.25.0
- Google Chrome 158
- Headless Chrome

## 3. Create a Test Website
Created a local website using an HTML file.

File:
`site/index.html`

Website content:
- Title: Screenshot Lab
- Heading: Screenshot Lab
- Paragraph: Static content.

## 4. Start the Local Web Server
Command:

```bash
cd site
python3 -m http.server 8000
```

The website was accessed at:

`http://localhost:8000/`

## 5. Open Website Using Selenium
Created a Python script named `shot.py`.

Used Selenium WebDriver to:
- Launch Chrome in headless mode.
- Open the local website.
- Read the page title and URL.

Verified output:

```text
Title/URL: Screenshot Lab http://localhost:8000/
```

## 6. Capture a Screenshot
Used Selenium's `save_screenshot()` method.

```python
driver.save_screenshot("screenshot.png")
```

Verified output:

```text
Screenshot saved: True
```

## 7. Verify Screenshot
Command:

```bash
ls -lh screenshot.png
file screenshot.png
```

Verified details:
- File: screenshot.png
- Format: PNG
- Resolution: 1280 x 657
- Color: RGB

## 8. Capture Timestamped Screenshots
Used Python's `time` module to create unique filenames.

```python
import time

timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = f"screenshot_{timestamp}.png"

driver.save_screenshot(filename)
```

Successfully created:

- screenshot_20261124-133340.png
- screenshot_20261124-133344.png

Both files were verified as PNG images.

## 9. Browser Cleanup
Used the following command in Python:

```python
driver.quit()
```

Verified:
- No Chrome processes running.
- Local server stopped.
- Chrome installer removed.

## 10. Important Commands
| Command | Purpose |
|---|---|
| `python shot.py` | Run Selenium script |
| `driver.get()` | Open webpage |
| `driver.save_screenshot()` | Capture screenshot |
| `time.strftime()` | Generate timestamp |
| `driver.quit()` | Close browser |
| `file screenshot.png` | Verify image format |

## 11. What I Learned
- How to launch Chrome in headless mode.
- How to open a local website using Selenium.
- How to capture webpage screenshots.
- How to create timestamped screenshot filenames.
- How to verify PNG files.
- How to close browser sessions safely.

## 12. Lab Result
Successfully completed the Selenium screenshot practical and verified three PNG screenshots.
