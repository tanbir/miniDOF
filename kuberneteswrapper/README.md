# KubernetesWrapper Class Documentation

A wrapper class for the Kubernetes Python client library.

## Installation

```bash
pip install kubernetes
```

## Usage

```python
from kubernetes_wrapper import KubernetesWrapper

# Create an instance of KubernetesWrapper
k8s = KubernetesWrapper()

# Print namespaces
print(k8s.list_namespaces())
```

## Functions

| Function Name       | Description                                     | Input                               | Output            |
|---------------------|-------------------------------------------------|-------------------------------------|-------------------|
| `list_pods`         | List pods in the specified namespace.          | `namespace: str = None`             | List of pod objects |
| `create_deployment` | Create a deployment.                            | `name: str`, `namespace: str`, `image: str`, `replicas: int = 1` | Deployment object |
| `delete_deployment` | Delete a deployment.                            | `name: str`, `namespace: str`       | None              |
| `list_deployments`  | List deployments in the specified namespace.   | `namespace: str = None`             | List of deployment objects |
| `create_service`    | Create a service.                              | `name: str`, `namespace: str`, `service_type: str`, `port: int`, `target_port: int` | Service object    |
| `delete_service`    | Delete a service.                              | `name: str`, `namespace: str`       | None              |
| `list_services`     | List services in the specified namespace.      | `namespace: str = None`             | List of service objects |
| `create_job`        | Create a job.                                  | `name: str`, `namespace: str`, `image: str`, `command: list`, `completions: int = 1`, `parallelism: int = 1` | Job object        |
| `delete_job`        | Delete a job.                                  | `name: str`, `namespace: str`       | None              |
| `list_jobs`         | List jobs in the specified namespace.          | `namespace: str = None`             | List of job objects |
| `create_config_map` | Create a ConfigMap.                            | `name: str`, `namespace: str`, `data: dict` | ConfigMap object  |
| `delete_config_map` | Delete a ConfigMap.                            | `name: str`, `namespace: str`       | None              |
| `list_config_maps`  | List ConfigMaps in the specified namespace.    | `namespace: str = None`             | List of ConfigMap objects |
| `create_secret`     | Create a Secret.                               | `name: str`, `namespace: str`, `data: dict` | Secret object     |
| `delete_secret`     | Delete a Secret.                               | `name: str`, `namespace: str`       | None              |
| `list_secrets`      | List Secrets in the specified namespace.      | `namespace: str = None`             | List of Secret objects |
| `create_namespace`  | Create a namespace.                            | `name: str`                         | Namespace object  |
| `delete_namespace`  | Delete a namespace.                            | `name: str`                         | None              |
| `list_namespaces`   | List namespaces.                               | None                                | List of namespace objects |

