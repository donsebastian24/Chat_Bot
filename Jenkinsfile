pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker')
    }
    stages {
        stage('Build Docker image') { 
            steps {
                node {
                    sh 'docker build -t don2421/chatbot:$BUILD_NUMBER .'
                }
            }
        }
        stage('login to dockerhub') {
            steps{
                node {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSM | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }
        stage('push image') {
            steps{
                node {
                    sh 'docker push don2421/chatbot:$BUILD_NUMBER'
                }
            }
        }
    }
    post {
        always {
            node {
                sh 'docker logout'
            }
        }
    }
}
