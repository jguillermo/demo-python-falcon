#!/usr/bin/env groovy

pipeline {
  agent any
  parameters {
    booleanParam(
      name: 'REGISTRY',
      defaultValue: false,
      description: "Requiere construir o no Registry in ECR")
    booleanParam(
      name: 'MIGRATIONS',
      defaultValue: false,
      description: "Indica si se ejecutaran las migraciones de DB")
    choice(
      name: 'ENV',
      choices:"dev\ndev3c\npre\npre3c\nprod",
      description: "Ambiente de despliegue")
    choice(
      name: 'DEPLOY_REGION',
      choices:"eu-west-1\nus-west-2\nus-east-1",
      description: "Region de despliegue de aws")
    choice(
      name: 'SLACK_CHANNEL',
      choices:"aptitus-dev-changelog\naptitus-pre-changelog\naptitus-changelog",
      description: "Canal de slack para notificar sobre el despliegue")
    choice(
      name: 'INFRA_BUCKET',
      choices:"infraestructura.dev\ninfraestructura.pre\ninfraestructura.prod",
      description: "Bucker de recursos para el despliegue")
    choice(
      name: 'MEMORY_SIZE',
      choices:"128\n256\n512\n768\n1024\n2048",
      description: "Cantidad de memoria asignada al contenedor")
    choice(
      name: 'DESIRED_COUNT',
      choices:"1\n2\n3\n4\n5\n10",
      description: "Numero ne instancias por incremento")
    text(name: 'MIN_SCALING',     defaultValue: '1',  description: 'Minimo de contenedores disponibles')
    text(name: 'MAX_SCALING',     defaultValue: '2',  description: 'Maximo de contenedores disponibles')
    text(name: 'HTTPS_PRIORITY',  defaultValue: '35', description: 'Prioridad de listener Https en el ALB: dev=35')
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Set Enviroment') {
      steps {
        sh '''
          export ENV=$ENV
          export DEPLOY_REGION=$DEPLOY_REGION
          export DESIRED_COUNT=$DESIRED_COUNT
          export MIN_SCALING=$MIN_SCALING
          export MAX_SCALING=$MAX_SCALING
          export HTTPS_PRIORITY=$HTTPS_PRIORITY
          export MEMORY_SIZE=$MEMORY_SIZE
          export INFRA_BUCKET=$INFRA_BUCKET
          export SLACK_CHANNEL=$SLACK_CHANNEL
          '''
      }
    }
    stage('ECR') {
      steps {
        script {
          if ("${params.REGISTRY}" == "true") {
            sh 'make create-registry'
          }
        }
      }
    }
    stage('Install') {
      steps {
        sh 'make install'
      }
    }
    stage('Sync CloudFormation Resources') {
      steps {
        sh 'make sync-cloudformation'
      }
    }
    stage('Build') {
      steps {
        sh 'make build-latest'
      }
    }
    stage('Publish') {
      steps {
        sh 'make publish'
      }
    }
    stage('Test') {
      steps {
        sh 'make tests'
      }
    }
    stage('DB Migrations') {
      steps {
        script {
          if ("${params.MIGRATIONS}" == "true") {
            sh 'make migrate'
          } else {
            echo 'no se ejecutaron las migraciones'
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'make update-service'
      }
    }
  }
  post {
    always {
      junit 'app/nosetests.xml'
      sh 'make chown'
    }
    success {
      sh '''
        make slack-notify SLACK_TITLE="Deploy realizado con éxito" SLACK_LINK=${JOB_URL} SLACK_TEXT="Se realizo de manera correcta el deploy del proyecto ${JOB_NAME} en la rama ${BRANCH_NAME}"
        '''
    }
    failure {
      sh '''
        make slack-notify SLACK_TITLE="Error de deploy" SLACK_LINK=${JOB_URL} SLACK_TEXT="Se presento un problema mientras se desplegaba el proyecto ${JOB_NAME} en la rama ${BRANCH_NAME}"
        '''
    }
  }
}
