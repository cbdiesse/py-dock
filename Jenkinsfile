pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t kaspy-app .'
        sh 'docker tag kaspy-app $DOCKER_BKASPY_IMAGE'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run kaspy-app python -m pytest tests'
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
          sh 'docker push $DOCKER_BKASPY_IMAGE'
        }
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
} 