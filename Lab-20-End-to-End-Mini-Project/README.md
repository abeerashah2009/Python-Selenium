# Lab 20 - End-to-End Mini Project

## 1. Lab Objective

The objective of this lab is to create a simple Demo Shop website and automate its search functionality using Python and Selenium WebDriver.

## 2. Tools and Technologies

- Ubuntu Linux
- Python 3.12.3
- Selenium 4.25.0
- Google Chrome 158.0.8127.88
- HTML
- JavaScript
- Chrome Headless Mode

## 3. Project Files

```text
Lab-20-End-to-End-Mini-Project/
│
├── evidence/
│   ├── screenshot.png
│   └── test-run.txt
│
├── index.html
├── test_shop.py
├── requirements.txt
├── screenshot.png
└── README.md
```

## 4. Python Environment Setup

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Install Selenium:

```bash
pip install selenium==4.25.0
```

Check the Selenium version:

```bash
python -c "import selenium; print(selenium.__version__)"
```

## 5. Google Chrome Installation

Download Chrome:

```bash
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Install Chrome:

```bash
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

Verify installation:

```bash
google-chrome --version
```

## 6. Create the Demo Shop Website

The `index.html` file contains:

- Demo Shop heading
- Search input field
- Search button
- JavaScript alert
- Success message
- Updated page title

Start the local web server:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Website address:

```text
http://127.0.0.1:8000/
```

## 7. Selenium Automation

The `test_shop.py` script automates the Demo Shop website.

The script performs these steps:

1. Opens Chrome in headless mode.
2. Loads the Demo Shop website.
3. Locates the search field using `By.NAME`.
4. Enters the search term `Dress`.
5. Clicks the Search button.
6. Waits for the JavaScript alert.
7. Verifies the alert text.
8. Accepts the alert.
9. Waits for the success message.
10. Takes a screenshot.
11. Verifies the updated page title.
12. Closes the browser using `driver.quit()`.

## 8. Run the Selenium Test

Run the automation script:

```bash
python test_shop.py
```

## 9. Verified Test Output

```text
Loaded: Demo Shop
Alert text: Searching for Dress
Success message: Success: results for Dress
Updated title: Search Results
All assertions passed.
```

All Selenium assertions passed successfully.

## 10. Screenshot and Evidence

The project contains:

- `screenshot.png` - Browser screenshot.
- `evidence/screenshot.png` - Screenshot evidence copy.
- `evidence/test-run.txt` - Test execution output.

The screenshot was verified as a valid PNG image.

## 11. Requirements File

The `requirements.txt` file contains:

```text
selenium==4.25.0
```

## 12. Cleanup

Stop the local server:

```bash
kill "$(cat server.pid)"
```

Deactivate the virtual environment:

```bash
deactivate
```

## 13. Learning Outcomes

After completing this lab, I learned:

- How to create a local HTML website.
- How to install and configure Selenium.
- How to automate Google Chrome.
- How to run Chrome in headless mode.
- How to locate web elements.
- How to use explicit waits.
- How to handle JavaScript alerts.
- How to verify page titles and success messages.
- How to capture screenshots as test evidence.
