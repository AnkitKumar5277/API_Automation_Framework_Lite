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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -n auto'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
