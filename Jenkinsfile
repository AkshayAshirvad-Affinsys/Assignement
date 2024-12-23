node {
    environment {
        NVD_API_KEY = 'bb6e5bca-bdfa-4c27-990e-b5da936d9f9f'  // Replace with your actual NVD API key
    }

    stage('OWASP-DEPENDENCY-CHECK') {
        dependencyCheck additionalArguments: ''' 
            -o './'
            -s './'
            -f 'ALL' 
            --prettyPrint
            --nvdApiKey $NVD_API_KEY''', 
            odcInstallation: 'OWASP-DEPENDENCY-CHECK'

        dependencyCheckPublisher pattern: 'dependency-check-report.xml'
    }
}
