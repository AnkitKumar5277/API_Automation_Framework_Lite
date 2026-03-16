pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/AnkitKumar5277/API_Automation_Framework_Lite.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -n auto --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }
    }
}
