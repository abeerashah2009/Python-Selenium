
# Lab 18 – File Upload Simulation

## 1. Introduction

This lab demonstrates how to automate a file upload using Python, Selenium, Firefox, and Flask.

A local Flask application provides the upload form. Selenium opens the page, selects a file, and submits it automatically.

## 2. Objectives

- Set up Selenium and Flask.
- Install Mozilla Firefox.
- Create a local file upload page.
- Locate a file input using Selenium.
- Upload a file through browser automation.
- Verify the uploaded file on the server.

## 3. Environment

- Operating System: Ubuntu 24.04 LTS
- Python: 3.12.3
- Selenium: 4.25.0
- Flask: 3.0.3
- Browser: Mozilla Firefox 161.0
- Browser mode: Headless

## 4. Project Files

| File or Folder | Purpose |
|---|---|
| app.py | Flask upload application |
| upload_simulation.py | Selenium automation script |
| sample.txt | Sample file for uploading |
| requirements.txt | Python dependencies |
| evidence.txt | Practical verification results |
| uploads/ | Stores uploaded files during testing |

## 5. Task 1 – Environment Setup

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install selenium==4.25.0 flask==3.0.3
```

Mozilla Firefox was installed from the official Mozilla APT repository.

## 6. Task 2 – Create the Flask Upload Page

The Flask application:

- Displays an HTML file upload form.
- Accepts file submissions through the POST method.
- Uses `secure_filename()` to sanitize the uploaded filename.
- Saves uploaded files in the `uploads/` directory.

Start the Flask application:

```bash
python app.py
```

The application listens on:

```text
http://127.0.0.1:5000/
```

## 7. Task 3 – Selenium File Upload

The Selenium script performs these actions:

1. Launches Firefox in headless mode.
2. Opens the local Flask upload page.
3. Finds the file input using its ID.
4. Selects the absolute path of `sample.txt`.
5. Finds and clicks the Upload button.
6. Waits for the upload confirmation.
7. Closes the browser.

Important Selenium commands:

```python
driver.get("http://localhost:5000/")

file_input = driver.find_element(By.ID, "fileInput")
file_input.send_keys(os.path.abspath("sample.txt"))

submit_button = driver.find_element(
    By.XPATH, '//button[@type="submit"]'
)
submit_button.click()
```

## 8. Task 4 – Upload Verification

Verify the uploaded file:

```bash
ls -l uploads/sample.txt
cat uploads/sample.txt
```

Check the Flask request log:

```bash
grep 'POST /upload' server.log
```

The upload was successful, and the server returned HTTP 200.

## 9. Important Concepts Learned

- Selenium WebDriver
- Firefox browser automation
- File input elements
- `send_keys()` for file selection
- XPath element location
- Explicit waits with `WebDriverWait`
- Flask routes and HTTP POST requests
- Secure filename handling
- Server-side file verification

## 10. How to Run the Project

Clone the repository and enter the lab directory:

```bash
git clone https://github.com/abeerashah2009/Python-Selenium.git
cd Python-Selenium/Lab-18-File-Upload-Simulation
```

Create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the Flask server:

```bash
nohup python app.py > server.log 2>&1 &
```

Run Selenium in an environment that does not select an older Snap geckodriver:

```bash
PATH="$VIRTUAL_ENV/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" python upload_simulation.py
```

Inspect the uploaded file:

```bash
cat uploads/sample.txt
```

## 11. Verified Results

- Flask upload page returned HTTP 200.
- Selenium selected `sample.txt`.
- Selenium submitted the upload form.
- Flask returned `Upload OK: sample.txt`.
- Uploaded file was verified on the server.
- Flask recorded a successful POST request with HTTP 200.
- Python syntax validation passed.
- Flask server shutdown was verified.

## 12. Conclusion

This lab demonstrated a complete automated file upload workflow using Selenium and Firefox with a local Flask application. It provided practical experience with browser automation, file handling, HTTP requests, and server-side verification.
