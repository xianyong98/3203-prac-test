pipeline {

    agent any

    environment { 
        CI = 'true'
    }

    stages {
        stage('Build') {
			steps {
				script {
					echo '-------- Performing Build Stage --------'
					try {
					    sh 'apt-get install python3'
					    sh 'apt install python3-pip'
					    sh 'python3 -m pip install pipenv'
						sh 'python3 -m pipenv install Pipfile'
						sh 'python3 -m pipenv run python3 flask run'
                        echo "Build has no errors! Proceeding on!"
                    } catch (Exception e) {
                        echo "Build has errors! Please check and verify!"
                    }
                }
            }
	}
	stage('SonarQube Analysis') {
            steps {
                script {
                    echo '-------- Performing SonarQube Scan --------'
                    def scannerHome = tool 'ict3x03_SonarQube_Scanner';
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                       echo "SonarQube Analysis has no errors! Proceeding on!"
                }
            }
        }

		// TAKE NOTE:
		// RUN THIS ONLY IN THE EVENT OF DOCKER SERVICE RESTART AS GOOGLE CHROME IS IN THE CONTAINER ALREADY. JUST NEED TO RUN ONCE!

//         stage('Setup Chrome') {
//            steps {
//                 echo '-------- Performing Chrome Setup Stage --------'
//                 sh 'apt-get update'
//				 sh 'apt --fix-broken install --assume-yes'
//                sh 'apt install wget'
//                 sh 'apt install -fy gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libnss3 lsb-release xdg-utils libgbm1'
//                 sh 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
//                 sh 'dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install'
//            }
//        }
        stage('Unit Test') {
            steps {
                script {
                    echo '-------- Performing Automated Unit Test Stage --------'
                    sh 'python3 -m pipenv run python3 ssdquiz/app.py test ssdquiz.tests.test_urls'
                    echo "Automated Unit Testing has no errors! Proceeding on!"
                }
            }
        }
	stage('Headless Browser Test') {
            steps {
                // Switch from production keys to test keys
                // Activation of Headless Script to allow captcha to run test keys
                echo '-------- Performing Headless Browser Test Stage --------'
                sh 'python3 -m pipenv run python3 ssdquiz/app.py test ssdquiz.tests.test_login'
                echo "Headless Browser Testing has no errors! Proceeding on!"
            }
        }
    }
}

