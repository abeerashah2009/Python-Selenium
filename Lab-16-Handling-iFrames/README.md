
# Lab 16 – Handling iFrames

## 1. Introduction

In this lab, I learned how to identify and interact with iFrames using Python and Selenium WebDriver.

An iFrame (Inline Frame) is an HTML element that displays another HTML page inside the main webpage.

Selenium needs to switch into an iFrame before accessing its internal elements.

## 2. Objectives

- Identify iFrames on a webpage.
- Find iFrame ID, name, and index.
- Switch between the main page and an iFrame.
- Interact with elements inside an iFrame.
- Return to the main page.
- Understand Selenium frame handling commands.

## 3. Lab Environment

- Operating System: Ubuntu 24.04.3 LTS
- Programming Language: Python 3.12.3
- Automation Tool: Selenium WebDriver 4.25.0
- Browser: Google Chrome 158
- Execution Mode: Headless

## 4. Project Files

| File | Description |
|---|---|
| main.html | Main webpage containing the iFrame |
| inner.html | HTML page displayed inside the iFrame |
| identify.py | Identifies available iFrames |
| switch.py | Switches into an iFrame |
| interact.py | Clicks a button inside the iFrame |
| full.py | Tests switching between the iFrame and main page |
| requirements.txt | Python dependencies |
| evidence.txt | Practical execution results |
| .gitignore | Excludes unnecessary files |

## 5. Understanding iFrames

An iFrame is a separate browsing context embedded inside a webpage.

For example, our main page contains an iFrame with:

- ID: exampleIframe
- Name: exampleFrame
- Index: 0

The Submit button is located inside the iFrame, not directly inside the main webpage.

## 6. Task 1 – Identify iFrames

First, I located all iFrames using:

```python
frames = driver.find_elements(By.TAG_NAME, "iframe")
```

To get the ID and name:

```python
frame.get_attribute("id")
frame.get_attribute("name")
```

Verified output:

```text
iFrames found: 1
Index: 0
ID: exampleIframe
Name: exampleFrame
Task 1 passed
```

## 7. Task 2 – Switch to an iFrame

Before switching, Selenium could not find the Submit button in the main page.

I used:

```python
driver.switch_to.frame("exampleFrame")
```

After switching, Selenium successfully found the button.

Verified output:

```text
button NOT found in main page
button found in iframe: Submit
Task 2 passed
```

## 8. Task 3 – Interact with an Element

I switched to the first iFrame using its index:

```python
driver.switch_to.frame(0)
```

Then I located and clicked the Submit button:

```python
driver.find_element(By.ID, "submitButton").click()
```

I checked the status before and after clicking.

Verified output:

```text
before: not clicked
after: clicked
Task 3 passed
```

## 9. Task 4 – Return to the Main Page

To return to the main webpage, I used:

```python
driver.switch_to.default_content()
```

I verified that the main page title was accessible and the Submit button inside the iFrame was no longer accessible from the main page.

Verified output:

```text
status in iframe: clicked
main title: Main Page
button not reachable from main (expected)
Task 4 passed
```

## 10. Important Selenium Commands

| Selenium Command | Purpose |
|---|---|
| find_elements(By.TAG_NAME, "iframe") | Find all iFrames |
| get_attribute("id") | Get iFrame ID |
| get_attribute("name") | Get iFrame name |
| switch_to.frame(0) | Switch using index |
| switch_to.frame("exampleFrame") | Switch using name |
| switch_to.default_content() | Return to main page |
| driver.quit() | Close browser session |

## 11. How to Run the Lab

Clone the repository:

```bash
git clone https://github.com/abeerashah2009/Python-Selenium.git
cd Python-Selenium/Lab-16-Handling-iFrames
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Selenium:

```bash
pip install -r requirements.txt
```

Run the practical scripts:

```bash
python identify.py
python switch.py
python interact.py
python full.py
```

## 12. Browser Cleanup

Each Python script uses:

```python
finally:
    driver.quit()
```

This ensures that the Selenium browser session is closed after the test finishes, including when an error occurs.

## 13. Key Learnings

1. An iFrame is a separate browsing context.
2. Selenium must switch into an iFrame before accessing its elements.
3. An iFrame can be selected using its ID, name, index, or WebElement.
4. The `default_content()` method returns Selenium to the main webpage.
5. The `driver.quit()` method closes the browser session.

## 14. Conclusion

Successfully completed all four practical tasks using Python and Selenium WebDriver.

I learned how to identify iFrames, switch between browsing contexts, interact with elements inside an iFrame, and return to the main webpage.
