# Lab 12 – Handling Dropdowns

## 1. Objective

The objective of this lab is to learn how to handle HTML dropdown menus using Selenium WebDriver in Python.

## 2. Tools Used

- Ubuntu 24.04
- Python 3.12.3
- Selenium 4.25.0
- Google Chrome 158
- HTML

## 3. Project Files

- `dropdown.html` – HTML page containing the dropdown menu.
- `dropdown.py` – Python script to automate dropdown selection.
- `.gitignore` – Excludes unnecessary files.
- `evidence.txt` – Practical execution evidence.

## 4. Understanding the HTML Dropdown

The dropdown contains three options:

| Option | Value |
|---|---|
| Option 1 | 1 |
| Option 2 | 2 |
| Option 3 | 3 |

Dropdown element:

```html
<select id="dropdown-example" name="options">
```

The `id` helps Selenium locate the dropdown.

## 5. Importing Selenium Select Class

```python
from selenium.webdriver.support.ui import Select
```

The `Select` class is used to interact with HTML dropdown menus.

## 6. Locating the Dropdown

```python
dropdown = driver.find_element(By.ID, "dropdown-example")
```

This command finds the dropdown using its ID.

## 7. Creating a Select Object

```python
select_element = Select(dropdown)
```

This creates a Select object so we can interact with the dropdown.

## 8. Selecting by Visible Text

```python
select_element.select_by_visible_text("Option 2")
```

This selects an option using the text displayed on the webpage.

## 9. Selecting by Value

```python
select_element.select_by_value("3")
```

This selects an option using its HTML value attribute.

## 10. Getting the Selected Option

```python
selected_option = select_element.first_selected_option
print(selected_option.text)
```

This retrieves the currently selected option's text.

## 11. Running the Python Script

```bash
python3 dropdown.py
```

### Verified Output

```text
After text select: Option 2
Selected option: Option 3
```

Both selection assertions passed successfully.

## 12. Python Syntax Verification

Command:

```bash
python3 -m py_compile dropdown.py
```

Result: Passed with no syntax errors.

## 13. Dropdown Options Verification

Command:

```bash
grep -o '<option ' dropdown.html | wc -l
```

Output:

```text
3
```

Three dropdown options were found.

## 14. Browser Cleanup

Command:

```bash
pgrep -x chrome >/dev/null && echo "Chrome still running" || echo "No Chrome processes left"
```

Output:

```text
No Chrome processes left
```

## 15. Key Learning Points

1. How to locate dropdown elements using Selenium.
2. How to use the `Select` class.
3. How to select options by visible text.
4. How to select options by value.
5. How to retrieve the selected option.
6. How to close the browser using `driver.quit()`.

## 16. Conclusion

Successfully completed the Selenium Handling Dropdowns practical.

Both dropdown selection methods were tested and verified successfully.
