{
    "app_name": "codeformuenster-redirect",
    "services": [
        {
            "service_name": "redirect-service",
            "components": [
                {
                    "component_name": "c4m-redirect",
                    "image": "registry.giantswarm.io/giantswarm/flaskexample",
                    "args": ["python", "manage.py runserver 0.0.0.0:8000"],
                    "ports": [ "8000/tcp" ],
                    "domains": { "c4mredirect.gigantic.io": "8000" }
                }
            ]
        }
    ]
}
