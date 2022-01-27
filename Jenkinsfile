pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    registry = ('shawaraa/courseapp')
    DOCKER_HUB_CREDENTIALS = credentials('dockerhubaccount') 
    AWS_CREDENTIALS = credentials('shawara-aws-cred')
    KEYCHAIN_PASSWORD = credentials('shawara-keychain')
    dockerImage = ''
  }
  stages {
    stage('Cloning Git') {
      steps {
        git branch: 'main', url: 'https://github.com/mahmoudshawara/Course-app.git'
      }
    }
    stage('Tooling versions') {
      steps {
        sh '''
          docker --version
          docker compose version
        '''
      }
    }
    stage('Build') {
      steps {
        sh 'docker context use default'
        script {
          dockerImage = docker.build registry + ":${env.BUILD_NUMBER}"
          docker.withRegistry( 'https://registry.hub.docker.com', 'DOCKER_HUB_CREDENTIALS' ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker context use myecscontext'
        sh 'docker compose up'
        sh 'docker compose ps --format json'
      }
    }
  }
}