pipeline {
    agent any
<<<<<<< HEAD

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                virtualenv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                . venv/bin/activate
                python test.py
                '''
            }
        }
    }
=======
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker')
    }
    stages {
        stage('Build Docker image') { 
            steps {
                script {
                    sh 'docker build -t don2421/chatbot:$BUILD_NUMBER .'
                }
            }
        }
        stage('login to dockerhub') {
            steps{
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSM | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }
        stage('push image') {
            steps{
                script {
                    sh 'docker push don2421/chatbot:$BUILD_NUMBER'
                }
            }
        }
    }
    
>>>>>>> origin/main
}
