pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Thirisha0306/Question3.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python main.py'
            }
        }
    }
}