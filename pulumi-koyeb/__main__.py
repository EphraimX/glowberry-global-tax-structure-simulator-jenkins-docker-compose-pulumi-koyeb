"""Pulumi Infrastructure for Glowberry Tax Simulator"""

import pulumi
import pulumi_koyeb as koyeb


glowberry_application = koyeb.App("gtaxsim-gha-dkr-plkb", name="gtaxsim-gha-dkr-plkb")

glowberry_application_service = koyeb.Service("gtaxsim-gha-dkr-plkb-service",

    app_name=glowberry_application.name,
    definition={
        "name": "gtaxsim-gha-dkr-plkb",
        "instance_types": [{
            "type": "nano",
        }],
        "ports": [{
            "port": 3000,
            "protocol": "http",
        }],
        "scalings": [{
            "min": 1,
            "max": 1,
        }],
        "envs": [
            {
                "key": "PORT",
                "value": "3000",
            },
        ],
        "routes": [{
            "path": "/",
            "port": 3000,
        }],
        "regions": ["fra"],
        "git": {
            "branch": "main",
            "repository": "github.com/EphraimX/glowberry-global-tax-structure-simulator-gha-docker-compose-pulumi-koyeb",
            "dockerfile": {
                "dockerfile": "Dockerfile.koyeb",
                "privileged": True,
            },
        },
    },
  opts = pulumi.ResourceOptions(depends_on=[glowberry_application])
)