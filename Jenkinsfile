pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 ./main_test.py'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}