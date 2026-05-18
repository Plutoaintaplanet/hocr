pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        DOCKER_IMAGE = 'plutoaintaplanet/hocr-app'
        DOCKER_TAG = "v${env.BUILD_ID}"
        DOCKER_REGISTRY_CREDENTIALS = 'docker-hub-credentials'
        RENDER_WEBHOOK_URL = credentials('deploy-webhook-url')
    }

    stages {
        stage('1. Checkout Source Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Plutoaintaplanet/hocr.git'
                echo "Source code fetched successfully from GitHub."
            }
        }

        stage('2. Code Quality Analysis') {
            steps {
                echo "Running SonarCloud Analysis..."
                script {
                    def scannerHome = tool 'SonarQubeScanner'
                    // Ensure 'SonarCloud' is configured in Jenkins System Settings
                    withSonarQubeEnv('SonarCloud') {
                        if (isUnix()) {
                            sh "${scannerHome}/bin/sonar-scanner"
                        } else {
                            bat "${scannerHome}/bin/sonar-scanner.bat"
                        }
                    }
                }
            }
        }

        stage('3. Dependency & Vulnerability Scanning') {
            steps {
                echo "Running Trivy Scanning using Docker..."
                script {
                    def trivyImage = 'ghcr.io/aquasecurity/trivy:canary'
                    if (isUnix()) {
                        sh "docker run --rm -v \$(pwd):/project ${trivyImage} fs --severity HIGH,CRITICAL --format table /project"
                        sh "docker run --rm -v \$(pwd):/project ${trivyImage} fs --severity HIGH,CRITICAL --format json -o /project/trivy-report.json /project"
                    } else {
                        bat "docker run --rm -v %cd%:/project ${trivyImage} fs --severity HIGH,CRITICAL --format table /project"
                        bat "docker run --rm -v %cd%:/project ${trivyImage} fs --severity HIGH,CRITICAL --format json -o /project/trivy-report.json /project"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'trivy-report.json', fingerprint: true
                }
            }
        }


        stage('4. Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    if (isUnix()) {
                        sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} -t ${DOCKER_IMAGE}:latest ."
                    } else {
                        bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} -t ${DOCKER_IMAGE}:latest ."
                    }
                }
            }
        }

        stage('5. Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing to Docker Hub..."
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        if (isUnix()) {
                            sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                            sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                            sh "docker push ${DOCKER_IMAGE}:latest"
                        } else {
                            bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                            bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                            bat "docker push ${DOCKER_IMAGE}:latest"
                        }
                    }
                }
            }
        }

        stage('6. Deploy to Public Cloud') {
            steps {
                echo "Deploying to Render..."
                script {
                    if (isUnix()) {
                        sh 'curl -X POST $RENDER_WEBHOOK_URL'
                    } else {
                        powershell "Invoke-RestMethod -Uri '${env.RENDER_WEBHOOK_URL}' -Method Post"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished execution."
        }
    }
}
