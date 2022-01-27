pipeline {
  agent any
  environment {
    registry = "shawara/courseapp"
    registryCredential = credentials('dockerhubaccount')
    AWS_CREDS = credentials('shawara-aws-cred')
    dockerImage = ''
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
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          docker.withRegistry( '', registryCredential  ) {
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