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
* **made with openclaude and chatgpt**

---

Install dependencies

```
pip install -r requirements.txt
```

---

# Running Tests

Run all tests

```
python -m venv venv
venv\Scripts\activate
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
scoop install allure
pytest --alluredir=allure-results
allure serve allure-results
```
---

Install all dependencies using:

```
pip install -r requirements.txt
```

---

Automation framework for **learning API testing using PyTest**.

## **VS Code With OpenCode :**  
<img width="1920" height="1080" alt="Screenshot 2026-03-16 233748" src="https://github.com/user-attachments/assets/7b8b5805-6dba-4da4-bd00-5687432f4552" />

## **Git & Github :**   
<img width="610" height="449" alt="Screenshot 2026-03-17 004718" src="https://github.com/user-attachments/assets/a7b3b54d-b770-4fae-9d13-12f945e9e992" />

## **Github :**  
<img width="1919" height="985" alt="Screenshot 2026-03-17 005025" src="https://github.com/user-attachments/assets/59c53560-f55a-4830-8343-86c847eb50fd" />

## **Allure Report :**  
<img width="1061" height="570" alt="image" src="https://github.com/user-attachments/assets/0f1ee079-cfbf-4564-ba67-ab832c2ca2a7" />


