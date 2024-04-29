from kubernetes import client, config
from kubernetes.client.rest import ApiException

class KubernetesWrapper:
    """
    A wrapper class for the Kubernetes Python client library.
    """

    def __init__(self):
        """
        Initialize the Kubernetes API client.
        """
        config.load_kube_config()
        self.core_api = client.CoreV1Api()
        self.apps_api = client.AppsV1Api()
        self.batch_api = client.BatchV1Api()
        self.custom_objects_api = client.CustomObjectsApi()

    def list_pods(self, namespace=None):
        """
        List pods in the specified namespace.

        Args:
            namespace (str, optional): Namespace to list pods from. Defaults to None (all namespaces).

        Returns:
            list: List of pod objects.
        """
        try:
            return self.core_api.list_namespaced_pod(namespace)
        except ApiException as e:
            print(f"Error listing pods: {e}")
            return []

    def create_deployment(self, name, namespace, image, replicas=1):
        """
        Create a deployment.

        Args:
            name (str): Name of the deployment.
            namespace (str): Namespace to deploy the application to.
            image (str): Docker image for the deployment.
            replicas (int, optional): Number of replicas. Defaults to 1.

        Returns:
            dict: Deployment object.
        """
        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "spec": {
                "replicas": replicas,
                "selector": {
                    "matchLabels": {"app": name}
                },
                "template": {
                    "metadata": {"labels": {"app": name}},
                    "spec": {"containers": [{"name": name, "image": image}]}
                }
            }
        }
        try:
            return self.apps_api.create_namespaced_deployment(namespace, body=deployment)
        except ApiException as e:
            print(f"Error creating deployment: {e}")
            return None

    def delete_deployment(self, name, namespace):
        """
        Delete a deployment.

        Args:
            name (str): Name of the deployment.
            namespace (str): Namespace of the deployment.
        """
        try:
            return self.apps_api.delete_namespaced_deployment(name, namespace)
        except ApiException as e:
            print(f"Error deleting deployment: {e}")
            return None

    def list_deployments(self, namespace=None):
        """
        List deployments in the specified namespace.

        Args:
            namespace (str, optional): Namespace to list deployments from. Defaults to None (all namespaces).

        Returns:
            list: List of deployment objects.
        """
        try:
            return self.apps_api.list_namespaced_deployment(namespace)
        except ApiException as e:
            print(f"Error listing deployments: {e}")
            return []

    def create_service(self, name, namespace, service_type, port, target_port):
        """
        Create a service.

        Args:
            name (str): Name of the service.
            namespace (str): Namespace to create the service in.
            service_type (str): Type of service (e.g., 'ClusterIP', 'NodePort', 'LoadBalancer').
            port (int): Port number.
            target_port (int): Target port number.

        Returns:
            dict: Service object.
        """
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "spec": {
                "type": service_type,
                "ports": [{"port": port, "targetPort": target_port}]
            }
        }
        try:
            return self.core_api.create_namespaced_service(namespace, body=service)
        except ApiException as e:
            print(f"Error creating service: {e}")
            return None

    def delete_service(self, name, namespace):
        """
        Delete a service.

        Args:
            name (str): Name of the service.
            namespace (str): Namespace of the service.
        """
        try:
            return self.core_api.delete_namespaced_service(name, namespace)
        except ApiException as e:
            print(f"Error deleting service: {e}")
            return None

    def list_services(self, namespace=None):
        """
        List services in the specified namespace.

        Args:
            namespace (str, optional): Namespace to list services from. Defaults to None (all namespaces).

        Returns:
            list: List of service objects.
        """
        try:
            return self.core_api.list_namespaced_service(namespace)
        except ApiException as e:
            print(f"Error listing services: {e}")
            return []

    def create_job(self, name, namespace, image, command, completions=1, parallelism=1):
        """
        Create a job.

        Args:
            name (str): Name of the job.
            namespace (str): Namespace to create the job in.
            image (str): Docker image for the job.
            command (list): Command to run in the job container.
            completions (int, optional): Number of completions. Defaults to 1.
            parallelism (int, optional): Parallelism. Defaults to 1.

        Returns:
            dict: Job object.
        """
        job = {
            "apiVersion": "batch/v1",
            "kind": "Job",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "spec": {
                "completions": completions,
                "parallelism": parallelism,
                "template": {
                    "metadata": {"name": name},
                    "spec": {
                        "containers": [{
                            "name": name,
                            "image": image,
                            "command": command
                        }],
                        "restartPolicy": "Never"
                    }
                }
            }
        }
        try:
            return self.batch_api.create_namespaced_job(namespace, body=job)
        except ApiException as e:
            print(f"Error creating job: {e}")
            return None

    def delete_job(self, name, namespace):
        """
        Delete a job.

        Args:
            name (str): Name of the job.
            namespace (str): Namespace of the job.
        """
        try:
            return self.batch_api.delete_namespaced_job(name, namespace)
        except ApiException as e:
            print(f"Error deleting job: {e}")
            return None

    def list_jobs(self, namespace=None):
        """
        List jobs in the specified namespace.

        Args:
            namespace (str, optional): Namespace to list jobs from. Defaults to None (all namespaces).

        Returns:
            list: List of job objects.
        """
        try:
            return self.batch_api.list_namespaced_job(namespace)
        except ApiException as e:
            print(f"Error listing jobs: {e}")
            return []

    def create_config_map(self, name, namespace, data):
        """
        Create a ConfigMap.

        Args:
            name (str): Name of the ConfigMap.
            namespace (str): Namespace to create the ConfigMap in.
            data (dict): Data for the ConfigMap.

        Returns:
            dict: ConfigMap object.


        """
        config_map = {
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "data": data
        }
        try:
            return self.core_api.create_namespaced_config_map(namespace, body=config_map)
        except ApiException as e:
            print(f"Error creating ConfigMap: {e}")
            return None

    def delete_config_map(self, name, namespace):
        """
        Delete a ConfigMap.

        Args:
            name (str): Name of the ConfigMap.
            namespace (str): Namespace of the ConfigMap.
        """
        try:
            return self.core_api.delete_namespaced_config_map(name, namespace)
        except ApiException as e:
            print(f"Error deleting ConfigMap: {e}")
            return None

    def list_config_maps(self, namespace=None):
        """
        List ConfigMaps in the specified namespace.

        Args:
            namespace (str, optional): Namespace to list ConfigMaps from. Defaults to None (all namespaces).

        Returns:
            list: List of ConfigMap objects.
        """
        try:
            return self.core_api.list_namespaced_config_map(namespace)
        except ApiException as e:
            print(f"Error listing ConfigMaps: {e}")
            return []

    def create_secret(self, name, namespace, data):
        """
        Create a Secret.

        Args:
            name (str): Name of the Secret.
            namespace (str): Namespace to create the Secret in.
            data (dict): Data for the Secret.

        Returns:
            dict: Secret object.
        """
        secret = {
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {
                "name": name,
                "namespace": namespace
            },
            "data": data
        }
        try:
            return self.core_api.create_namespaced_secret(namespace, body=secret)
        except ApiException as e:
            print(f"Error creating Secret: {e}")
            return None

    def delete_secret(self, name, namespace):
        """
        Delete a Secret.

        Args:
            name (str): Name of the Secret.
            namespace (str): Namespace of the Secret.
        """
        try:
            return self.core_api.delete_namespaced_secret(name, namespace)
        except ApiException as e:
            print(f"Error deleting Secret: {e}")
            return None

    def list_secrets(self, namespace=None):
        """
        List Secrets in the specified namespace.

        Args:
            namespace (str, optional): Namespace to list Secrets from. Defaults to None (all namespaces).

        Returns:
            list: List of Secret objects.
        """
        try:
            return self.core_api.list_namespaced_secret(namespace)
        except ApiException as e:
            print(f"Error listing Secrets: {e}")
            return []

    def create_namespace(self, name):
        """
        Create a namespace.

        Args:
            name (str): Name of the namespace.

        Returns:
            dict: Namespace object.
        """
        namespace = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": name}
        }
        try:
            return self.core_api.create_namespace(body=namespace)
        except ApiException as e:
            print(f"Error creating namespace: {e}")
            return None

    def delete_namespace(self, name):
        """
        Delete a namespace.

        Args:
            name (str): Name of the namespace.
        """
        try:
            return self.core_api.delete_namespace(name)
        except ApiException as e:
            print(f"Error deleting namespace: {e}")
            return None

    def list_namespaces(self):
        """
        List namespaces.

        Returns:
            list: List of namespace objects.
        """
        try:
            return self.core_api.list_namespace()
        except ApiException as e:
            print(f"Error listing namespaces: {e}")
            return []

    def apply_manifest(self, manifest):
        """
        Apply Kubernetes manifest.

        Args:
            manifest (dict): Kubernetes manifest.

        Returns:
            dict: Applied object.
        """
        try:
            return self.custom_objects_api.create_namespaced_custom_object(
                group="apps",
                version="v1",
                namespace=manifest["metadata"]["namespace"],
                plural="deployments",
                body=manifest
            )
        except ApiException as e:
            print(f"Error applying manifest: {e}")
            return None

    def delete_resource(self, resource_type, name, namespace=None):
        """
        Delete a Kubernetes resource.

        Args:
            resource_type (str): Type of the Kubernetes resource (e.g., "deployment", "service").
            name (str): Name of the resource.
            namespace (str, optional): Namespace of the resource. Defaults to None.

        Returns:
            bool: True if the resource is deleted successfully, False otherwise.
        """
        try:
            if resource_type == "deployment":
                return self.apps_api.delete_namespaced_deployment(name, namespace)
            elif resource_type == "service":
                return self.core_api.delete_namespaced_service(name, namespace)
            # Add more resource types as needed...
        except ApiException as e:
            print(f"Error deleting resource: {e}")
            return False

    def get_resource(self, resource_type, name, namespace=None):
        """
        Get details of a Kubernetes resource.

        Args:
            resource_type (str): Type of the Kubernetes resource (e.g., "deployment", "service").
            name (str): Name of the resource.
            namespace (str, optional): Namespace of the resource. Defaults to None.

        Returns:
            dict: Details of the resource.
        """
        try:
            if resource_type == "deployment":
                return self.apps_api.read_namespaced_deployment(name, namespace)
            elif resource_type == "service":
                return self.core_api.read_namespaced_service(name, namespace)
            # Add more resource types as needed...
        except ApiException as e:
            print(f"Error getting resource: {e}")
            return None

    def list_resources(self, resource_type, namespace=None):
        """
        List Kubernetes resources of a specific type.

        Args:
            resource_type (str): Type of the Kubernetes resource (e.g., "deployment", "service").
            namespace (str, optional): Namespace of the resource. Defaults to None.

        Returns:
            list: List of resources.
        """
        try:
            if resource_type == "deployment":
                return self.apps_api.list_namespaced_deployment(namespace)
            elif resource_type == "service":
                return self.core_api.list_namespaced_service(namespace)
            # Add more resource types as needed...
        except ApiException as e:
            print(f"Error listing resources: {e}")
            return []