pipeline {
    agent {
        label "worker"
    }
    
    parameters {
        string(name: 'GIT_URL', defaultValue: 'https://github.com/.../project_name.git', description: 'URL for GitHub repository')
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Branch for GitHub repository')
        string(name: 'DOCKER_IMAGE', defaultValue: 'username/repo_name:version', description: 'Image for DockerHub')
    }
    
    environment {
        DOCKER_REGISTRY_URL = 'https://registry.hub.docker.com/'
        DOCKER_CREDENTIALS_ID = 'dockerhub-cred'
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git url: "${GIT_URL}",
                        branch: "${GIT_BRANCH}",
                        credentialsId: 'github-cred'
                }
            }
        }
        stage('Build docker image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Run test in docker image'){
            steps {
                script {
                    try {
                        sh 'docker run ${DOCKER_IMAGE} run test'
                    }
                    catch (Exception e) {
                        echo 'Tests failed'
                        currentBuild.result = 'FAILURE'
                        error('Stopping pipeliune due to Docker Image tests failed!')
                    }
                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    try {
                        docker.withRegistry("${DOCKER_REGISTRY_URL}", "${DOCKER_CREDENTIALS_ID}") {
                            echo 'Logged in Docker Hub'
                        }
                    }
                    catch (Exception e) {
                        echo 'Failed to login to Docker Hub'
                        currentBuild.result = 'FAILURE'
                        error('Stopping pipeliune due to Docker login failure!')
                    }
                }
            }
        }
        stage('Push Docker image') {
            steps {
                script {
                    docker.withRegistry("${DOCKER_REGISTRY_URL}", "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }
    }
}