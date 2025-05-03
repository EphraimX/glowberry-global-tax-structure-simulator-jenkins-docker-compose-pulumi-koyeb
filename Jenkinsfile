pipeline{

  agent any

  environment {
    KOYEB_API_TOKEN = credentials('KOYEB_TOKEN')
    PULUMI_ACCESS_TOKEN = credentials('PULUMI_ACCESS_TOKEN')
  }

  stages {

    stage('Pulumi Setup and Deploy Koyeb'){

      steps{
        dir('pulumi-koyeb') {
          sh '''
          apt update
          apt install -y software-properties-common
          add-apt-repository ppa:deadsnakes/ppa -y
          apt install python3.12 -y
          curl -fsSL https://get.pulumi.com | sh
          mkdir -p ~/.pulumi/plugins/resource-koyeb-v0.1.11
          curl -L https://github.com/koyeb/pulumi-koyeb/releases/download/v0.1.11/pulumi-resource-koyeb-v0.1.11-linux-amd64.tar.gz | tar -xz -C ~/.pulumi/plugins/resource-koyeb-v0.1.11
          export PATH=$HOME/.pulumi/bin:$PATH
          pulumi login
          pulumi stack select glowberry-dev-gha-stack || pulumi stack init glowberry-dev-gha-stack
          pulumi preview
          pulumi up -y
          '''
        }

      }
    }

  }
}