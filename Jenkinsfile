pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    registry = "shawara/courseapp"
    registryCredential = credentials('dockerhubaccount')
    AWS_CREDS = credentials('shawara-aws-cred')
    dockerImage = ''
  }
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/mahmoudshawara/Course-app.git'
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
    stage('PreBuild') {
      steps {
        sh 'docker context use default'
        echo ">>>>>>>>> Start Clearing old docker images"
        sh '''
          if docker images -a | grep "shawara*" | awk '{print $1":"$2}' | xargs docker rmi -f; then
            printf 'Clearing old images succeeded\n'
          else
            printf 'Clearing old images failed\n'
          fi
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