pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sudo apt-get install python3
            }
        }
        
        stage('Test') {
            steps {
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
