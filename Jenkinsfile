pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    registry = "shawara/courseapp"
    DOCKER_HUB_CREDS = credentials('dockerhubaccount')
    AWS_CREDS = credentials('shawara-aws-cred')
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
          docker.withRegistry( 'https://index.docker.io/v1/', DOCKER_HUB_CREDS ) {
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