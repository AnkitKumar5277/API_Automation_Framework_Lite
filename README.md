python -m venv venv

venv\Scripts\activate

scoop install allure

pytest --alluredir=allure-results
