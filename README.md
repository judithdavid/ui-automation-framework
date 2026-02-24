# UI Automation Framework (Selenium + PyTest)

## Overview

This project is a modular UI automation framework built using Selenium WebDriver and PyTest.

It demonstrates Page Object Model (POM) design, explicit wait synchronization, reusable driver factory, and environment-based configuration.

---

## Tech Stack

- Python 3.x
- Selenium
- PyTest
- WebDriverManager

---

## Framework Structure
```
automation-framework/
│
├── config/            
├── pages/             
├── tests/            
├── utils/             
├── conftest.py        
├── requirements.txt
└── README.md
```
---

## Key Features

- Page Object Model (POM)
- Explicit wait synchronization
- Headless execution support
- Environment-based configuration
- Clean setup and teardown via fixtures
- Modular and scalable structure

---

## Test Coverage

- Valid login
- Add product to cart flow

---

## Setup

1. Create virtual environment:

   python -m venv venv

2. Activate:

   Windows:
   venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Run tests:

   pytest