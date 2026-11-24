# Lab 08 - Checking Page Title & Content

## 1. Objective
Learn how to use Selenium to check a web page title and validate page content.

## 2. Tools Used
- Ubuntu 24.04
- Python 3.12
- Selenium 4.25.0
- Mozilla Firefox
- Geckodriver
- HTML

## 3. Project Files
- index.html - Local test webpage
- title_check.py - Selenium page title and link text test
- title_fail.py - Negative assertion test

## 4. HTML Test Page
Created a local HTML page containing:
- Page title: Welcome to Al-Nafi Lab
- Heading: Selenium Practice Page
- Link text: Downloads

## 5. Selenium Browser Setup
- Imported Selenium WebDriver.
- Configured Firefox in headless mode.
- Disabled browser proxy settings for local testing.
- Opened the local webpage using driver.get().

## 6. Checking Page Title
Used driver.title to read the page title.

Expected title:
Welcome to Al-Nafi Lab

Used assert to compare the actual title with the expected title.

## 7. Locating Page Elements
Used By.XPATH to locate the Downloads link.

Validated its text using element.text.

## 8. Closing the Browser
Used driver.quit() inside a finally block to close the browser safely.

## 9. Negative Assertion Test
Changed the expected title to Wrong Title.

The test correctly raised an AssertionError because the actual page title did not match.

## 10. Learning Outcomes
- Read page titles with Selenium.
- Locate elements using XPath.
- Validate text using assertions.
- Run Firefox in headless mode.
- Close WebDriver safely.
- Test both successful and failed assertions.
