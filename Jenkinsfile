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
        		sh 'python3 -m pydoc -w trivia'
        		sh 'mv trivia.html /var/www/html/documentins/trivia.html'
   			}
		}
		stage('Send Email') {
            steps {
                emailext(
                    subject: "Actualización en Trivia",
                    body: "Se acaba de hacer una actualización en el repositorio del proyecto de Trivia. Para ver la nueva documentación vaya a http://ec2-34-201-54-91.compute-1.amazonaws.com",
                    to: "rsotelosilva@gmail.com",
                    from: "rsotelosilva@gmail.com"
                )
            }
        }
        
	}
}
