pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/rsotelo14/pa-trivia.git', branch: 'main'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh '/usr/bin/python3 -m unittest discover -s test'
            }
        }
        stage('Generar Documentación') {
            steps {
                sh 'sudo mkdir -p /opt/docs && sudo chmod 777 /opt/docs'
                
                sh 'cd src && python3 -m pydoc -w main'
                
                sh 'sudo mv src/main.html /var/www/html/documentins/trivia.html'
            }
        }
    }
}
