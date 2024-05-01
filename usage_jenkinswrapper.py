
from jenkinswrapper.jenkinswrapper import JenkinsWrapper

jenkins_server_url = 'http://localhost:8080'
jenkins_username = 'admin'
jenkins_password = 'admin123'

jenkins_wrapper = JenkinsWrapper(jenkins_server_url, jenkins_username, jenkins_password)

# Get the Jenkins server info
print("Jenkins Server Info:", jenkins_wrapper.get_server_info())

# Get the current user info
print("Current User Info:", jenkins_wrapper.get_user_info())

# Create a new job
job_name = 'test-job'
config_xml = jenkins.EMPTY_CONFIG_XML

# Create the job
print("Creating Job:", jenkins_wrapper.create_job(job_name, config_xml))

# Get all jobs
print("All Jobs:", jenkins_wrapper.get_all_jobs())

# Get job info
print("Job Info:", jenkins_wrapper.get_job_info(job_name))

# Trigger a build
print("Triggering Build:", jenkins_wrapper.trigger_build(job_name))

# Get last build info
last_build_info = jenkins_wrapper.get_last_build_info(job_name)
print("Last Build Info:", last_build_info)

# Get all nodes
print("All Nodes:", jenkins_wrapper.get_all_nodes())

# Get all views
print("All Views:", jenkins_wrapper.get_views())

# Get all plugins info
print("All Plugins Info:", jenkins_wrapper.get_plugins_info())

# Get computer info
print("Computer Info:", jenkins_wrapper.get_computer_info())





