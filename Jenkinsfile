pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    environment {
        SONAR_PROJECT_KEY = 'LLMOPS'
        SONAR_SCANNER_HOME = tool 'Sonarqubenew'
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'myrepo'
        IMAGE_TAG = "${env.BUILD_NUMBER ?: 'latest'}"
        DOCKER_BUILDKIT = '1'
    }

    stages {
        stage('Quality & Build') {
            parallel {
                stage('SonarQube Analysis') {
                    steps {
                        withCredentials([string(credentialsId: 'sonarqube-token-new', variable: 'SONAR_TOKEN')]) {
                            withSonarQubeEnv('Sonarqube-new') {
                                sh """
                                ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                                  -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                                  -Dsonar.sources=. \
                                  -Dsonar.host.url=http://sonarqube-dind:9000 \
                                  -Dsonar.login=${SONAR_TOKEN}
                                """
                            }
                        }
                    }
                }

                stage('Build and Push Docker Image to ECR') {
                    steps {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
                            script {
                                def accountId = sh(script: "aws sts get-caller-identity --query Account --output text", returnStdout: true).trim()
                                def ecrUrl = "${accountId}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"

                                sh """
                                aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ecrUrl}
                                docker build \
                                  --cache-from ${ecrUrl}:latest \
                                  --build-arg BUILDKIT_INLINE_CACHE=1 \
                                  -t ${ecrUrl}:${IMAGE_TAG} \
                                  -t ${ecrUrl}:latest \
                                  .
                                docker push ${ecrUrl}:${IMAGE_TAG}
                                docker push ${ecrUrl}:latest
                                """
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy to ECS Fargate') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
                    sh """
                    aws ecs update-service \
                      --cluster multi-ai-agent-final \
                      --service multi-ai-agent-new-final-service-41ipjj9j \
                      --force-new-deployment \
                      --region ${AWS_REGION}
                    """
                }
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed — check stage logs above.'
        }
        success {
            echo "Deployed image ${ECR_REPO}:${IMAGE_TAG} to ECS."
        }
    }
}