from mini_docker.wrapper import DockerWrapper

# Instantiate the GitWrapper class
wrapper = DockerWrapper()

# List containers
print(wrapper.list_containers())

# List services
print(wrapper.list_services())

# List configs
print(wrapper.list_configs())