pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    registry = "shawaraa/courseapp"
    DOCKER_HUB_CREDS = credentials('dockerhubaccount')
    AWS_CREDS = credentials('shawara-aws-cred')
    KEYCHAIN_PASSWORD = credentials('shawara-keychain')
    myImage = ''
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
        withCredentials([usernamePassword( credentialsId: 'DOCKER_HUB_CREDS', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) 
        docker.withRegistry('', 'docker-hub-credentials') {
          sh "docker login -u ${USERNAME} -p ${PASSWORD}"
          myImage.push("${env.BUILD_NUMBER}")
          myImage.push("latest")
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