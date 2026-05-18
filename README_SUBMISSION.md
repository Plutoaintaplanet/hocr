# DevOps Lab Exercise: CI/CD Pipeline Submission

## 1. Jenkinsfile Scripts
- **Full Pipeline (with Docker Push):** [Jenkinsfile](./Jenkinsfile)
- **Pipeline without Docker Push:** [Jenkinsfile-no-push](./Jenkinsfile-no-push)

## 2. GitHub Repository
- **URL:** [https://github.com/Plutoaintaplanet/hocr.git](https://github.com/Plutoaintaplanet/hocr.git)

## 3. Code Quality Analysis Report
- **Tool:** SonarCloud
- **Details:** The analysis is performed in the `2. Code Quality Analysis` stage. Reports are automatically uploaded to SonarCloud.
- **Dashboard:** [https://sonarcloud.io/dashboard?id=Plutoaintaplanet_hocr](https://sonarcloud.io/dashboard?id=Plutoaintaplanet_hocr)

## 4. Dependency/Vulnerability Scanning Report
- **Tool:** Trivy
- **Details:** The scanning is performed in the `3. Dependency & Vulnerability Scanning` stage. 
- **Output:** A detailed `trivy-report.json` is generated and archived as a build artifact in Jenkins for every run.
- **Console:** High-level results are also printed in the Jenkins build console in table format.

## 5. Docker Hub Image Link
- **URL:** [https://hub.docker.com/r/plutoaintaplanet/hocr-app](https://hub.docker.com/r/plutoaintaplanet/hocr-app)

## 6. Public Deployment & Frontend Dashboard
- **App URL:** [https://hocr-app.onrender.com](https://hocr-app.onrender.com)
- **Features:** A modern, visually appealing dashboard that showcases the 7-step CI/CD pipeline process in real-time, providing links to all audit reports and registry images.

## 7. Pipeline Execution Logs/Screenshots
- **Logs:** Accessible via the Jenkins Blue Ocean interface or the Build Console Output for each respective pipeline.
- **Triggers:** Both pipelines are configured with `githubPush()` triggers to automatically execute on every commit to the `main` branch.
