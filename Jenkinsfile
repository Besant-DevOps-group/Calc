pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                withPython(version: '3.8.5') {
                    sh 'python --version'
                }
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 ./main_test.py'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }
}
