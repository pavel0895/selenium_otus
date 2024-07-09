pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/pavel0895/selenium_otus/'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Black Formatter') {
            steps {
                sh '''
                    . venv/bin/activate
                    black .
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }
        stage('Reports') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    post {
        always {
            sh '''
                [ -n "$VIRTUAL_ENV" ] && . venv/bin/deactivate || true
            '''
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}