# Beginner Project 2: E-commerce Product and Cart Testing

A beginner-level Selenium WebDriver + Python + PyTest project using the public SauceDemo practice website.

## Test scenarios
1. Verify that the Products page opens after login.
2. Sort products from Z to A and verify the first product.
3. Add Sauce Labs Backpack to the cart and verify the cart count and product name.

Public demo credentials:
- Username: `standard_user`
- Password: `secret_sauce`

Do not use personal credentials.

## Requirements
- Python 3.10+
- Google Chrome
- Internet connection

## Setup on Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

Selenium 4 normally manages the Chrome driver automatically through Selenium Manager.

## Project structure
```text
beginner_selenium_product_cart_project/
├── pages/
│   ├── __init__.py
│   └── inventory_page.py
├── tests/
│   ├── __init__.py
│   └── test_product_cart.py
├── conftest.py
└── requirements.txt
```

## Concepts practised
- Selenium WebDriver
- ID and class-name locators
- Dropdown handling with Selenium Select
- PyTest tests and assertions
- Browser fixture using setup and teardown
- Basic Page Object Model

This is a learning project. Run it, understand each method and test, and make a small change yourself before adding it to your resume.
