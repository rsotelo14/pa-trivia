pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/rsotelo14/pa-trivia.git', branch: 'master'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh '/usr/bin/python3 -m unittest test.py'
            }
        }
		stage('Generar Documentación') {
    		steps {
        		sh 'mkdir -p /opt/docs && chmod 777 /opt/docs'
        		sh 'cd src && python3 -m pydoc -w main'
        		sh 'mv src/main.html /var/www/html/documentins/trivia.html'
   			}
		}

        
	}
}
