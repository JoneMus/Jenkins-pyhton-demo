pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Preparing the environment...'

                // HOX! If running Jenkins on Windows without Docker, 
                // change "sh" to "bat" commands below.
                
                // Install dependencies
                sh 'pip install -r requirements.txt' 
            }
        }
        
        stage('Testing & Quality') {
            steps {
                echo 'Running tests...'
                // Running tests and generate xml report for Jenkins
                sh 'pytest --junitxml=test-results.xml --cov=src tests/'
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml'
            echo 'Pipe completed.'
        }
    }
}