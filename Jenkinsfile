pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                pip install python3
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing the project...'
                python3 ./main_test.py
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }
}
