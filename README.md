# API Automation Framework (PyTest)

A beginner-friendly **API Automation Testing Framework** built using **Python, PyTest, and Requests**.
The framework supports **Data Driven Testing (CSV)**, **Parallel Execution**, and **CI/CD using Jenkins**.

---

# Project Structure

```
api-automation-framework
│
├── src
│   ├── constants        # API endpoints and constants
│   ├── helpers          # Request helpers and CSV reader
│   ├── data             # CSV test data files
│   ├── tests            # Test cases
│   └── utils            # Utility functions
│
├── conftest.py          # PyTest fixtures
├── pytest.ini           # PyTest configuration
├── requirements.txt     # Project dependencies
├── Jenkinsfile          # CI/CD pipeline
└── README.md
```

---

# Features

* API Automation using **PyTest**
* **Requests Library** for API calls
* **CSV Data Driven Testing**
* **Parallel Test Execution (pytest-xdist)**
* **Fixtures for reusable setup**
* **Allure Reporting**
* **CI/CD Integration with Jenkins**

---

# Installation

Clone the repository

```
git clone <repo-url>
cd api-automation-framework
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running Tests

Run all tests

```
pytest
```

Run tests in **parallel**

```
pytest -n auto
```

Run with **Allure report**

```
pytest --alluredir=allure-results
```

Generate report

```
allure serve allure-results
```

---

# Data Driven Testing

Test data is stored in:

```
src/data/booking_data.csv
```

Tests read CSV data and execute the same test with multiple inputs.

---

# CI/CD (Jenkins)

The project includes a **Jenkinsfile** to automate:

1. Code checkout
2. Dependency installation
3. Test execution
4. Allure report generation

---

# Requirements

* Python 3.8+
* PyTest
* Requests
* pytest-xdist
* Allure

Install all dependencies using:

```
pip install -r requirements.txt
```

---

# Author

Automation framework for **learning API testing using PyTest**.


python -m venv venv

venv\Scripts\activate

scoop install allure

pytest --alluredir=allure-results
