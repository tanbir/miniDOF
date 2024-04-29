import docker

class DockerWrapper:
    """
    A wrapper class for Docker functionalities.
    """

    def __init__(self):
        """
        Initializes the Docker client.
        """
        self.client = docker.from_env()

    def list_containers(self):
        """
        Lists all Docker containers.

        Returns:
        - list: A list of container dictionaries.
        """
        return self.client.containers.list()

    def create_container(self, image, command=None):
        """
        Creates a new Docker container.

        Parameters:
        - image (str): The image to use for the new container.
        - command (list): The command to run in the container.

        Returns:
        - str: The ID of the created container.
        """
        return self.client.containers.run(image, command)

    def stop_container(self, container_id):
        """
        Stops a running Docker container.

        Parameters:
        - container_id (str): The ID of the container to stop.
        """
        container = self.client.containers.get(container_id)
        container.stop()

    def remove_container(self, container_id):
        """
        Removes a Docker container.

        Parameters:
        - container_id (str): The ID of the container to remove.
        """
        container = self.client.containers.get(container_id)
        container.remove()

    def list_images(self):
        """
        Lists all Docker images.

        Returns:
        - list: A list of image dictionaries.
        """
        return self.client.images.list()

    def pull_image(self, image):
        """
        Pulls a Docker image from a registry.

        Parameters:
        - image (str): The name of the image to pull.

        Returns:
        - str: The ID of the pulled image.
        """
        return self.client.images.pull(image)

    def inspect_image(self, image):
        """
        Inspects a Docker image.

        Parameters:
        - image (str): The name or ID of the image to inspect.

        Returns:
        - dict: A dictionary containing image metadata.
        """
        return self.client.images.get(image).attrs

    def build_image(self, path, tag):
        """
        Builds a Docker image from a Dockerfile.

        Parameters:
        - path (str): The path to the directory containing the Dockerfile.
        - tag (str): The tag to assign to the built image.

        Returns:
        - str: The ID of the built image.
        """
        return self.client.images.build(path=path, tag=tag)

    def push_image(self, repository, tag=None):
        """
        Pushes a Docker image to a registry.

        Parameters:
        - repository (str): The name of the repository to push the image to.
        - tag (str): The tag of the image to push.

        Returns:
        - bool: True if the push was successful, False otherwise.
        """
        return self.client.images.push(repository, tag=tag)

    def list_volumes(self):
        """
        Lists all Docker volumes.

        Returns:
        - list: A list of volume dictionaries.
        """
        return self.client.volumes.list()

    def create_volume(self, name):
        """
        Creates a Docker volume.

        Parameters:
        - name (str): The name of the volume to create.
        """
        return self.client.volumes.create(name)

    def remove_volume(self, name):
        """
        Removes a Docker volume.

        Parameters:
        - name (str): The name of the volume to remove.
        """
        volume = self.client.volumes.get(name)
        volume.remove()

    def list_networks(self):
        """
        Lists all Docker networks.

        Returns:
        - list: A list of network dictionaries.
        """
        return self.client.networks.list()

    def create_network(self, name, driver=None):
        """
        Creates a Docker network.

        Parameters:
        - name (str): The name of the network to create.
        - driver (str): The driver to use for the network (default is bridge).
        """
        return self.client.networks.create(name, driver=driver)

    def remove_network(self, name):
        """
        Removes a Docker network.

        Parameters:
        - name (str): The name of the network to remove.
        """
        network = self.client.networks.get(name)
        network.remove()

    def prune_containers(self):
        """
        Prunes unused Docker containers.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.containers.prune()

    def prune_images(self):
        """
        Prunes unused Docker images.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.images.prune()

    def prune_volumes(self):
        """
        Prunes unused Docker volumes.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.volumes.prune()

    def prune_networks(self):
        """
        Prunes unused Docker networks.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.networks.prune()

    def attach_to_container(self, container_id, logs=False, stream=False):
        """
        Attaches to a running Docker container.

        Parameters:
        - container_id (str): The ID of the container to attach to.
        - logs (bool): Whether to retrieve container logs (default is False).
        - stream (bool): Whether to stream logs in real-time (default is False).

        Returns:
        - str: The logs if logs=True and stream=False.
        """
        container = self.client.containers.get(container_id)
        if logs:
            return container.logs(stream=stream)
        else:
            return container.attach(stream=stream)

    # New functionalities

    def create_service(self, image, name, ports=None):
        """
        Creates a Docker service.

        Parameters:
        - image (str): The image to use for the service.
        - name (str): The name of the service to create.
        - ports (dict): A dictionary mapping container ports to host ports.

        Returns:
        - str: The ID of the created service.
        """
        ports = ports or {}
        return self.client.services.create(image, name=name, ports=ports)

    def list_services(self):
        """
        Lists all Docker services.

        Returns:
        - list: A list of service dictionaries.
        """
        return self.client.services.list()

    def remove_service(self, service_id):
        """
        Removes a Docker service.

        Parameters:
        - service_id (str): The ID of the service to remove.
        """
        service = self.client.services.get(service_id)
        service.remove()

    def inspect_service(self, service_id):
        """
        Inspects a Docker service.

        Parameters:
        - service_id (str): The ID of the service to inspect.

        Returns:
        - dict: A dictionary containing service metadata.
        """
        return self.client.services.get(service_id).attrs

    def exec_command(self, container_id, command):
        """
        Executes a command inside a Docker container.

        Parameters:
        - container_id (str): The ID of the container.
        - command (str): The command to execute.

        Returns:
        - tuple: A tuple containing exit code and output of the command.
        """
        container = self.client.containers.get(container_id)
        return container.exec_run(command)

    def create_secret(self, name, data):
        """
        Creates a Docker secret.

        Parameters:
        - name (str): The name of the secret.
        - data (str): The secret data.

        Returns:
        - str: The ID of the created secret.
        """
        return self.client.secrets.create(name=name, data=data)

    def list_secrets(self):
        """
        Lists all Docker secrets.

        Returns:
        - list: A list of secret dictionaries.
        """
        return self.client.secrets.list()

    def remove_secret(self, secret_id):
        """
        Removes a Docker secret.

        Parameters:
        - secret_id (str): The ID of the secret to remove.
        """
        secret = self.client.secrets.get(secret_id)
        secret.remove()

    def create_config(self, name, data):
        """
        Creates a Docker config.

        Parameters:
        - name (str): The name of the config.
        - data (str): The config data.

        Returns:
        - str: The ID of the created config.
        """
        return self.client.configs.create(name=name, data=data)

    def list_configs(self):
        """
        Lists all Docker configs.

        Returns:
        - list: A list of config dictionaries.
        """
        return self.client.configs.list()

    def remove_config(self, config_id):
        """
        Removes a Docker config.

        Parameters:
        - config_id (str): The ID of the config to remove.
        """
        config = self.client.configs.get(config_id)
        config.remove()

    def get_stats(self, container_id):
        """
        Get real-time statistics of a Docker container.

        Parameters:
        - container_id (str): The ID of the container.

        Returns:
        - dict: A dictionary containing real-time statistics of the container.
        """
        container = self.client.containers.get(container_id)
        return container.stats(stream=False)

    def rename_container(self, container_id, new_name):
        """
        Renames a Docker container.

        Parameters:
        - container_id (str): The ID of the container to rename.
        - new_name (str): The new name for the container.
        """
        container = self.client.containers.get(container_id)
        container.rename(new_name)

    def prune_secrets(self):
        """
        Prunes unused Docker secrets.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.secrets.prune()

    def prune_configs(self):
        """
        Prunes unused Docker configs.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.configs.prune()

    def prune_services(self):
        """
        Prunes unused Docker services.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.services.prune()

    def prune_nodes(self):
        """
        Prunes unused Docker nodes.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.nodes.prune()

    def prune_builds(self):
        """
        Prunes unused Docker builds.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.api.prune_builds()

    def prune_system(self):
        """
        Prunes unused Docker system resources.

        Returns:
        - dict: A dictionary containing the results of the pruning operation.
        """
        return self.client.api.prune_system()

    def get_node(self, node_id):
        """
        Gets information about a Docker node.

        Parameters:
        - node_id (str): The ID of the node.

        Returns:
        - dict: A dictionary containing information about the node.
        """
        return self.client.nodes.get(node_id).attrs

    def list_nodes(self):
        """
        Lists all Docker nodes.

        Returns:
        - list: A list of node dictionaries.
        """
        return self.client.nodes.list()
