# DockerWrapper Class Documentation

The DockerWrapper class provides a convenient wrapper for interacting with Docker containers, images, networks, and other Docker resources using the Docker Python SDK.

## Installation

Install the Docker SDK for Python using pip:

```bash
pip install docker
```

## Usage

```python
from docker_wrapper import DockerWrapper

# Create an instance of the DockerWrapper class
docker_wrapper = DockerWrapper()

# Use DockerWrapper methods to interact with Docker resources
```

## DockerWrapper Functions

| Function Name       | Description                                           | Inputs                                | Outputs                               |
|---------------------|-------------------------------------------------------|---------------------------------------|---------------------------------------|
| `__init__`          | Initializes the Docker client                         | None                                  | None                                  |
| `list_containers`   | Lists all Docker containers                           | None                                  | List of container dictionaries        |
| `create_container`  | Creates a new Docker container                        | image (str), command (list)           | ID of the created container           |
| `stop_container`    | Stops a running Docker container                      | container_id (str)                    | None                                  |
| `remove_container`  | Removes a Docker container                            | container_id (str)                    | None                                  |
| `list_images`       | Lists all Docker images                               | None                                  | List of image dictionaries            |
| `pull_image`        | Pulls a Docker image from a registry                  | image (str)                           | ID of the pulled image                |
| `inspect_image`     | Inspects a Docker image                               | image (str)                           | Image metadata dictionary             |
| `build_image`       | Builds a Docker image from a Dockerfile               | path (str), tag (str)                 | ID of the built image                 |
| `push_image`        | Pushes a Docker image to a registry                   | repository (str), tag (str)           | True if push was successful           |
| `list_volumes`      | Lists all Docker volumes                              | None                                  | List of volume dictionaries           |
| `create_volume`     | Creates a Docker volume                               | name (str)                            | None                                  |
| `remove_volume`     | Removes a Docker volume                               | name (str)                            | None                                  |
| `list_networks`     | Lists all Docker networks                             | None                                  | List of network dictionaries         |
| `create_network`    | Creates a Docker network                              | name (str), driver (str)              | None                                  |
| `remove_network`    | Removes a Docker network                              | name (str)                            | None                                  |
| `prune_containers`  | Prunes unused Docker containers                      | None                                  | Prune results dictionary              |
| `prune_images`      | Prunes unused Docker images                          | None                                  | Prune results dictionary              |
| `prune_volumes`     | Prunes unused Docker volumes                         | None                                  | Prune results dictionary              |
| `prune_networks`    | Prunes unused Docker networks                        | None                                  | Prune results dictionary              |
| `attach_to_container`| Attaches to a running Docker container               | container_id (str), logs (bool), stream (bool) | Logs or attach output          |
| `create_service`    | Creates a Docker service                              | image (str), name (str), ports (dict) | ID of the created service             |
| `list_services`     | Lists all Docker services                             | None                                  | List of service dictionaries         |
| `remove_service`    | Removes a Docker service                              | service_id (str)                      | None                                  |
| `inspect_service`   | Inspects a Docker service                             | service_id (str)                      | Service metadata dictionary           |
| `exec_command`      | Executes a command inside a Docker container          | container_id (str), command (str)    | Exit code and output tuple            |
| `create_secret`     | Creates a Docker secret                               | name (str), data (str)               | ID of the created secret              |
| `list_secrets`      | Lists all Docker secrets                              | None                                  | List of secret dictionaries          |
| `remove_secret`     | Removes a Docker secret                               | secret_id (str)                       | None                                  |
| `create_config`     | Creates a Docker config                               | name (str), data (str)               | ID of the created config              |
| `list_configs`      | Lists all Docker configs                              | None                                  | List of config dictionaries          |
| `remove_config`     | Removes a Docker config                               | config_id (str)                       | None                                  |
| `get_stats`         | Get real-time statistics of a Docker container        | container_id (str)                   | Real-time statistics dictionary      |
| `rename_container`  | Renames a Docker container                            | container_id (str), new_name (str)   | None                                  |
| `prune_secrets`     | Prunes unused Docker secrets                          | None                                  | Prune results dictionary              |
| `prune_configs`     | Prunes unused Docker configs                          | None                                  | Prune results dictionary              |
| `prune_services`    | Prunes unused Docker services                         | None                                  | Prune results dictionary              |
| `prune_nodes`       | Prunes unused Docker nodes                            | None                                  | Prune results dictionary              |
| `prune_builds`      | Prunes unused Docker builds                           | None                                  | Prune results dictionary              |
| `prune_system`      | Prunes unused Docker system resources                | None                                  | Prune results dictionary              |
| `get_node`          | Gets information about a Docker node                  | node_id (str)                         | Node metadata dictionary              |
| `list_nodes`        | Lists all Docker nodes                                | None                                  | List of node dictionaries            |


