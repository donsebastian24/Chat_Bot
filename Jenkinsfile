pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker')
    }
    stages {

        stage('login to dockerhub') {
            steps{
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSM | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }
        stage('cloning Git'){
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: []])

                }
            }
        stage('Build Docker image') {
            steps {
                script {
                    sh 'docker build -t don2421/chatbot:$BUILD_NUMBER .'
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
    node('any') {
    // some block
    post {
        always {
            script {
                sh 'docker logout'
            }
        }
    }
}


}




