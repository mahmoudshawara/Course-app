pipeline {
  agent { label 'windows' }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKER_HUB_CREDS = credentials('docker-hub-account')
    AWS_CREDS = credentials('shawara-aws-cred')
  }
  stages {
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
        sh 'docker compose build'
        sh 'docker compose push'
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