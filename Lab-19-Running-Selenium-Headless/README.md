# Lab 19 – Running Selenium Headless

## 1. Lab Objective

The objective of this lab is to understand how to run Selenium WebDriver in two browser modes:

- **Headless Mode:** Runs Chrome without displaying a graphical browser window.
- **Headed Mode:** Runs Chrome with a graphical interface.

We also compare execution time and Chrome memory usage in both modes.

## 2. Technologies Used

- Python 3.12
- Selenium 4.25.0
- Google Chrome for Testing 158.0.8127.88
- ChromeDriver 158.0.8127.88
- psutil 7.2.2
- Xvfb (Virtual Display)
- Ubuntu Linux

## 3. Project Structure

```text
Lab-19-Running-Selenium-Headless/
│
├── evidence/
│   ├── headless-screenshot.png
│   ├── headed-screenshot.png
│   ├── headless-run.txt
│   └── headed-run.txt
│
├── headless.py
├── index.html
├── requirements.txt
├── .gitignore
└── README.md
```

## 4. Install Dependencies

Install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate

pip install selenium==4.25.0 psutil==7.2.2
```

Install Xvfb for headed browser testing on a server without a physical display:

```bash
sudo apt install -y xvfb
```

## 5. Create a Local Webpage

We created a local HTML webpage for Selenium testing.

The local web server runs on port 8000.

Check the webpage:

```bash
curl -I http://127.0.0.1:8000
```

Expected result:

```text
HTTP/1.0 200 OK
```

## 6. Configure Chrome Headless Mode

Selenium uses ChromeOptions to configure browser behavior.

Example:

```python
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
```

The `--headless=new` argument starts Chrome without displaying a graphical browser window.

## 7. Run Headless Mode

Command:

```bash
python headless.py headless
```

The script performs the following tasks:

1. Starts Chrome in headless mode.
2. Opens the local webpage.
3. Reads the page title.
4. Measures execution time.
5. Saves a screenshot.
6. Measures Chrome process memory usage.
7. Closes the browser.

Verified page title:

```text
Selenium Headless Lab
```

Screenshot:

`evidence/headless-screenshot.png`

## 8. Run Headed Mode Using Xvfb

A Linux server may not have a physical display.

Xvfb provides a virtual display that allows graphical applications to run without a physical monitor.

Command:

```bash
xvfb-run -a python headless.py headed
```

This runs Chrome in headed mode inside the virtual display.

Screenshot:

`evidence/headed-screenshot.png`

## 9. Performance Comparison

The following measurements were recorded during the final evidence runs.

| Measurement | Headless | Headed with Xvfb |
|---|---:|---:|
| Execution time | 1.92 seconds | 1.49 seconds |
| Chrome processes | 13 | 13 |
| Total Chrome RSS | 1120.22 MB | 1288.38 MB |
| Screenshot | Passed | Passed |

Note: Execution time and memory usage can change between runs depending on system resources and browser startup conditions.

## 10. Screenshots and Evidence

The evidence folder contains:

- `headless-screenshot.png` – Screenshot captured in headless mode.
- `headed-screenshot.png` – Screenshot captured in headed mode.
- `headless-run.txt` – Headless execution output.
- `headed-run.txt` – Headed execution output.

Both screenshots were verified as valid PNG images with a resolution of 1280 × 600.

## 11. Important Concepts

### Headless Browser

A browser that runs without a visible graphical interface.

### Headed Browser

A browser that runs with a graphical interface.

### Xvfb

X Virtual Framebuffer provides a virtual display for graphical applications on Linux servers.

### ChromeDriver

ChromeDriver allows Selenium WebDriver to communicate with Google Chrome.

### psutil

Python library used to inspect running processes and measure system resource usage.

### RSS (Resident Set Size)

RSS represents the physical memory currently occupied by a process.

## 12. Learning Outcomes

After completing this lab, I learned how to:

- Configure Selenium ChromeOptions.
- Run Chrome in headless mode.
- Run Chrome in headed mode using Xvfb.
- Capture browser screenshots.
- Measure browser execution time.
- Monitor Chrome process memory using psutil.
- Use Selenium Manager to detect Chrome and obtain a matching ChromeDriver.

## 13. Conclusion

This lab demonstrated how Selenium can automate Chrome in both headless and headed modes.

Headless mode is useful for automated testing on servers and CI/CD pipelines where a graphical interface is not required.

Xvfb makes headed browser testing possible on Linux systems without a physical display.

Both browser modes successfully opened the local webpage and generated screenshots.
