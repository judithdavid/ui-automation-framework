# UI Automation Framework

Production-grade UI automation framework built using Selenium WebDriver and PyTest with Page Object Model (POM), reusable BasePage architecture, structured logging, screenshot capture, environment-driven configuration, and GitHub Actions CI integration.

---

# Tech Stack

- Python 3.12
- Selenium WebDriver
- PyTest
- WebDriver Manager
- Python Dotenv
- GitHub Actions

---

# Framework Architecture

```text
ui-automation-framework/
│
├── config/
│   └── config.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_negative.py
│
├── utils/
│   ├── driver_factory.py
│   └── logger.py
│
├── logs/
│
├── screenshots/
│
├── reports/
│
├── .github/
│   └── workflows/
│       └── ui-tests.yml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Key Features

- Page Object Model (POM)
- Reusable BasePage architecture
- Explicit wait synchronization
- Structured logging
- Automatic screenshot capture on test failures
- Headless execution support
- Environment-based configuration using `.env`
- Smoke and regression test tagging
- GitHub Actions CI integration
- Modular and scalable framework design

---

# Logging System

The framework supports configurable logging levels through `.env`.

## INFO Mode

Logs:
- Page navigation
- Element interactions
- Test execution flow

## DEBUG Mode

Can be extended to log:
- Locator details
- Wait states
- Browser information
- Additional debugging traces

Logs are written to:
- Terminal output
- `logs/test.log`

---

# Screenshot Capture

The framework automatically captures screenshots on test failures.

Screenshots are stored inside:

```text
screenshots/
```

---

# Test Coverage

The framework currently validates:

- Valid login workflow
- Add product to cart workflow
- Invalid login validation
- Negative cart validation

---

# Environment Configuration

Create a `.env` file in the project root:

```env
ENV=qa

HEADLESS=true

APP_USERNAME=standard_user
APP_PASSWORD=secret_sauce

LOG_LEVEL=INFO
```

---

# Installation

## 1. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run all tests

```bash
pytest -v
```

---

## Run smoke tests

```bash
pytest -m smoke
```

---

## Run regression tests

```bash
pytest -m regression
```

---

# CI/CD

The framework includes GitHub Actions integration for automated test execution on every push and pull request.

---

# Example Logs

```text
2026-05-18 13:10:03,866 | INFO | pages.base_page | Clicking element: ('id', 'login-button')
```

---

# Engineering Highlights

- Reusable Selenium action layer
- Centralized configuration management
- Structured logging strategy
- Screenshot-based debugging support
- Environment-driven execution
- CI-ready architecture
- Maintainable and scalable framework design