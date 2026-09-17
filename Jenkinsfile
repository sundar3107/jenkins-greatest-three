pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t greatest-three:1.0 .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm greatest-three:1.0'
            }
        }
    }
}