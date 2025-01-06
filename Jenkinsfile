pipeline {
    agent any
    
    stages {
        
        
        stage('Dependency Track Publisher') {
            steps {
                withCredentials([string(credentialsId: 'AUTO-API', variable: 'API_KEY')]) {
                    dependencyTrackPublisher artifact: 'sbom.json', autoCreateProjects: true, projectName: 'CI-analytics-test', projectVersion: '1.0', dependencyTrackApiKey: API_KEY, projectId: '', synchronous: true
                }
            }
        }
    }
}
