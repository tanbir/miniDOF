## JenkinsWrapper Class

The `JenkinsWrapper` class provides a Python wrapper for interacting with Jenkins through its REST API.

### Installation

To use the `JenkinsWrapper` class, follow these steps:

1. Install the `jenkins` Python package:

```bash
pip install python-jenkins
```


### Functions

| Function Name                 | Description                                                             | Input                                         | Output                                |
|-------------------------------|-------------------------------------------------------------------------|-----------------------------------------------|---------------------------------------|
| `get_server_info()`          | Get information about the Jenkins server.                               | None                                          | dict: Server information             |
| `get_user_info()`            | Get information about the currently authenticated user.                | None                                          | dict: User information               |
| `create_job(job_name, config_xml)` | Create a new job in Jenkins.                                           | job_name (str): Name of the job<br>config_xml (str): XML configuration of the job | None                              |
| `get_all_jobs()`             | Get information about all Jenkins jobs.                                 | None                                          | list: List of dictionaries containing information about each job |
| `get_job_info(job_name)`     | Get information about a specific Jenkins job.                           | job_name (str): Name of the job               | dict: Information about the job     |
| `get_last_build_info(job_name)` | Get information about the last build of a Jenkins job.                  | job_name (str): Name of the job               | dict: Information about the last build |
| `trigger_build(job_name)`    | Trigger a build for a specific Jenkins job.                             | job_name (str): Name of the job               | dict: Response from Jenkins         |
| `get_build_info(job_name, build_number)` | Get information about a specific build of a job.                   | job_name (str): Name of the job<br>build_number (int): Build number | dict: Information about the build  |
| `get_build_console_output(job_name, build_number)` | Get the console output of a specific build of a Jenkins job.   | job_name (str): Name of the job<br>build_number (int): Build number | str: Console output of the build   |
| `get_build_test_report(job_name, build_number)` | Get the test report for a specific build of a job.                 | job_name (str): Name of the job<br>build_number (int): Build number | dict: Test report for the build    |
| `get_job_config(job_name)`   | Get the configuration of a job in XML format.                          | job_name (str): Name of the job               | str: XML configuration of the job   |
| `reconfig_job(job_name, config_xml)` | Reconfigure a job with the provided XML configuration.            | job_name (str): Name of the job<br>config_xml (str): XML configuration of the job | dict: Response from Jenkins         |
| `get_builds(job_name, depth=1)` | Get information about all builds of a job.                          | job_name (str): Name of the job<br>depth (int, optional): Depth of the builds to retrieve. Defaults to 1. | list: Information about all builds of the job |
| `copy_job(job_name, new_job_name)` | Copy a job in Jenkins.                                             | job_name (str): Name of the existing job<br>new_job_name (str): Name of the new job to create as a copy | dict: Response from Jenkins         |
| `enable_job(job_name)`       | Enable a job in Jenkins.                                                | job_name (str): Name of the job               | dict: Response from Jenkins         |
| `disable_job(job_name)`      | Disable a job in Jenkins.                                               | job_name (str): Name of the job               | dict: Response from Jenkins         |
| `trigger_parameterized_build(job_name, parameters)` | Trigger a parameterized build for a job in Jenkins.             | job_name (str): Name of the job<br>parameters (dict): Dictionary containing the parameters for the build | dict: Response from Jenkins         |
| `delete_job(job_name)`       | Delete a job from Jenkins.                                               | job_name (str): Name of the job               | dict: Response from Jenkins         |
| `create_view(view_name, view_description)` | Create a new view in Jenkins.                                     | view_name (str): Name of the view<br>view_description (str): Description of the view | dict: Response from Jenkins         |
| `add_jobs_to_view(view_name, jobs)` | Add one or more jobs to a view.                                  | view_name (str): The name of the view to which jobs will be added<br>jobs (list of dict): List of dictionaries with 'name' key representing job names | bool: True if jobs were successfully added to the view, False otherwise |
| `get_views()`                 | Get a list of all views in Jenkins.                                     | None                                          | list: List of views in Jenkins     |
| `get_view_config(view_name)` | Get the configuration of a specific view in Jenkins.                     | view_name (str): Name of the view             | str: XML configuration of the view |
| `delete_view(view_name)`     | Delete a view from Jenkins.                                              | view_name (str): Name of the view             | dict: Response from Jenkins         |
| `get_queue_info()`           | Get information about the Jenkins queue.                                 | None                                          | list: Information about the items in the Jenkins queue |
| `get_plugins_info()`         | Get information about installed plugins in Jenkins.                      | None                                          | list: Information about installed plugins |
| `create_node(name, num_executors=2, node_description=None, remote_fs='/var/lib/jenkins', labels='')` | Create a new node in Jenkins. | name (str): Name of the new node<br>num_executors (int): Number of executors for the node (default is 2)<br>node_description (str): Description of the node (default is None)<br>remote_fs (str): Remote filesystem root directory (default is '/var/lib/jenkins')<br>labels (str): Labels assigned to the node (default is '') | bool: True if the node creation was successful, False otherwise |
| `enable_node(node_name)`     | Enable a node in Jenkins.                                                 | node_name (str): Name of the node             | bool: True if the node was enabled successfully, False otherwise |
| `disable_node(node_name)`    | Disable a node in Jenkins.                                                | node_name (str): Name of the node             | bool: True if the node was disabled successfully, False otherwise |
| `get_all_nodes()`             | Get information about all nodes in the Jenkins environment.               | None                                          | list: Information about all nodes   |

### Usage Example

```python
from JenkinsWrapper import JenkinsWrapper

# Initialize JenkinsWrapper with server URL, username, and password
jenkins_wrapper = JenkinsWrapper("http://localhost:8080", "admin", "password")

# Get information about the Jenkins server
print("Server Info:", jenkins_wrapper.get_server_info())

# Get information about the currently authenticated user
print("User Info:", jenkins_wrapper.get_user_info())

# Get information about all Jenkins jobs
print("All Jobs:", jenkins_wrapper.get_all_jobs())

# Create a new job
job_name = "NewJob"
config_xml = '<your_job_configuration_xml>'
jenkins_wrapper.create_job(job_name, config_xml)

# Get information about a specific Jenkins job
print("Job Info:", jenkins_wrapper.get_job_info(job_name))

# Trigger a build for a specific Jenkins job
print("Trigger Build:", jenkins_wrapper.trigger_build(job_name))

# Get information about the last build of a Jenkins job
print("Last Build Info:", jenkins_wrapper.get_last_build_info(job_name))
```
