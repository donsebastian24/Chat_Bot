pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This will checkout your repo
                git branch: 'main', url: 'https://github.com/donsebastian24/Chat_Bot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // This will build your Docker image
                    dockerImage = docker.build "chatbot"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // This will push your Docker image to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'don2421', passwordVariable: 'Vandananickal@2421')]) {
                        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                            dockerImage.push("Project")
                        }
                    }
                }
            }
        }

        stage('Deploy to AWS') {
            steps {
                script {
                    // This will deploy your Docker image to an AWS instance
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-credentials', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                        sh '''
                        aws ecs register-task-definition --cli-input-json file://task-definition.json
                        aws ecs update-service --service your-service --task-definition your-task-definition --cluster your-cluster
                        '''
                    }
                }
            }
        }
    }
}
