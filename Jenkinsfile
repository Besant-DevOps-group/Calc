pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'echo nila | sudo -S apt-get install python3'
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
