import jenkins

class JenkinsWrapper:
    def __init__(self, server_url, username, password):
        """
        Initialize JenkinsWrapper with server URL, username, and password.

        Args:
            server_url (str): URL of the Jenkins server.
            username (str): Username for authentication.
            password (str): Password for authentication.
        """
        self.server_url = server_url
        self.username = username
        self.password = password
        self.server = jenkins.Jenkins(server_url, username=username, password=password)

    def get_server_info(self):
        """
        Get information about the Jenkins server.

        Returns:
            dict: Server information.
        """
        return self.server.get_version()

    def get_user_info(self):
        """
        Get information about the currently authenticated user.

        Returns:
            dict: User information.
        """
        # Get whoami information
        whoami_info = self.server.get_whoami()
        # Extract relevant user information
        user_info = {
            'id': whoami_info['id'],
            'absoluteUrl': whoami_info['absoluteUrl'],
            'fullName': whoami_info['fullName'],
            'description': whoami_info['description']
        }
        return user_info
      
    def create_job(self, job_name, config_xml=jenkins.EMPTY_CONFIG_XML):
        return self.server.create_job(job_name, config_xml)

    def get_all_jobs(self):
        """
        Get information about all Jenkins jobs.

        Returns:
            list: List of dictionaries containing information about each job.
        """
        return self.server.get_jobs()

    def get_job_info(self, job_name):
        """
        Get information about a specific Jenkins job.

        Args:
            job_name (str): Name of the job.

        Returns:
            dict: Information about the job.
        """
        return self.server.get_job_info(job_name)

    def get_last_build_info(self, job_name):
        """
        Get information about the last build of a Jenkins job.

        Args:
            job_name (str): Name of the job.

        Returns:
            dict: Information about the last build.
        """
        return self.server.get_job_info(job_name)['lastBuild']

    def trigger_build(self, job_name):
        """
        Trigger a build for a specific Jenkins job.

        Args:
            job_name (str): Name of the job to trigger the build for.

        Returns:
            dict: Response from Jenkins after triggering the build.
        """
        return self.server.build_job(job_name)

    def get_build_info(self, job_name, build_number):
        """
        Get information about a specific build of a job.

        Args:
            job_name (str): Name of the job.
            build_number (int): Build number.

        Returns:
            dict: Information about the build.
        """
        return self.server.get_build_info(job_name, build_number)

    def get_build_console_output(self, job_name, build_number):
        """
        Get the console output of a specific build of a Jenkins job.

        Args:
            job_name (str): Name of the job.
            build_number (int): Build number.

        Returns:
            str: Console output of the build.
        """
        return self.server.get_build_console_output(job_name, build_number)

    def get_build_test_report(self, job_name, build_number):
        """
        Get the test report for a specific build of a job.

        Args:
            job_name (str): Name of the job.
            build_number (int): Build number.

        Returns:
            dict: Test report for the build.
        """
        return self.server.get_build_test_report(job_name, build_number)

    def get_job_config(self, job_name):
        """
        Get the configuration of a job in XML format.

        Args:
            job_name (str): Name of the job.

        Returns:
            str: XML configuration of the job.
        """
        return self.server.get_job_config(job_name)

    def reconfig_job(self, job_name, config_xml=jenkins.RECONFIG_XML):
        """
        Reconfigure a job with the provided XML configuration.

        Args:
            job_name (str): Name of the job.
            config_xml (str): XML configuration of the job.

        Returns:
            dict: Response from Jenkins after reconfiguring the job.
        """
        return self.server.reconfig_job(job_name, config_xml)

    def get_builds(self, job_name, depth=1):
        """
        Get information about all builds of a job.

        Args:
            job_name (str): Name of the job.
            depth (int, optional): Depth of the builds to retrieve. Defaults to 1.

        Returns:
            list: Information about all builds of the job.
        """
        return self.server.get_builds(job_name, depth)

    def copy_job(self, job_name, new_job_name):
        """
        Copy a job in Jenkins.

        Args:
            job_name (str): Name of the existing job.
            new_job_name (str): Name of the new job to create as a copy.

        Returns:
            dict: Response from Jenkins after copying the job.
        """
        config_xml = self.get_job_config(job_name)
        return self.create_job(new_job_name, config_xml)

    def enable_job(self, job_name):
        """
        Enable a job in Jenkins.

        Args:
            job_name (str): Name of the job to enable.

        Returns:
            dict: Response from Jenkins after enabling the job.
        """
        return self.server.enable_job(job_name)

    def disable_job(self, job_name):
        """
        Disable a job in Jenkins.

        Args:
            job_name (str): Name of the job to disable.

        Returns:
            dict: Response from Jenkins after disabling the job.
        """
        return self.server.disable_job(job_name)

    def trigger_parameterized_build(self, job_name, parameters):
        """
        Trigger a parameterized build for a job in Jenkins.

        Args:
            job_name (str): Name of the job to trigger the build.
            parameters (dict): Dictionary containing the parameters for the build.

        Returns:
            dict: Response from Jenkins after triggering the parameterized build.
        """
        return self.server.build_job(job_name, parameters)

    def delete_job(self, job_name):
        """
        Delete a job from Jenkins.

        Args:
            job_name (str): Name of the job to delete.

        Returns:
            dict: Response from Jenkins after deleting the job.
        """
        return self.server.delete_job(job_name)


    def create_view(self, view_name, view_description):
        """
        Create a new view in Jenkins.

        Args:
            view_name (str): Name of the view to create.
            view_description (str): Description of the view.

        Returns:
            dict: Response from Jenkins after creating the view.
        """
        return self.server.create_view(view_name, view_description)

    def add_jobs_to_view(self, view_name, jobs):
        """
        Add one or more jobs to a view.

        Args:
            view_name (str): The name of the view to which jobs will be added.
            jobs (list of dict): List of dictionaries with 'name' key representing job names.

        Returns:
            bool: True if jobs were successfully added to the view, False otherwise.
        """
        try:
            # Get existing view configuration
            view_config = self.get_view_config(view_name)
            
            # Parse the XML configuration
            root = ElementTree.fromstring(view_config.encode())

            # Find the jobs element
            jobs_element = root.find('.//jobNames')

            # Add new jobs to the jobs element
            for job in jobs:
                job_name = job.get('name')
                if job_name and job_name not in jobs_element.text.split(','):
                    jobs_element.text += ',' + job_name
            
            # Update the view configuration
            updated_config = ElementTree.tostring(root, encoding='unicode')

            # Reconfigure the view with updated configuration
            self.reconfig_job(view_name, updated_config)

            return True
        except Exception as e:
            print(f"Error adding jobs to view: {e}")
            return False

    def get_views(self):
        """
        Get a list of all views in Jenkins.

        Returns:
            list: List of views in Jenkins.
        """
        return self.server.get_views()

    def get_view_config(self, view_name):
        """
        Get the configuration of a specific view in Jenkins.

        Args:
            view_name (str): Name of the view.

        Returns:
            str: XML configuration of the view.
        """
        return self.server.get_view_config(view_name)

    def delete_view(self, view_name):
        """
        Delete a view from Jenkins.

        Args:
            view_name (str): Name of the view to delete.

        Returns:
            dict: Response from Jenkins after deleting the view.
        """
        return self.server.delete_view(view_name)

    def get_queue_info(self):
        """
        Get information about the Jenkins queue.

        Returns:
            list: Information about the items in the Jenkins queue.
        """
        return self.server.get_queue_info()

    def get_plugins_info(self):
        """
        Get information about installed plugins in Jenkins.

        Returns:
            list: Information about installed plugins.
        """
        return self.server.get_plugins_info()

    def create_node(self, name, num_executors=2, node_description=None, remote_fs='/var/lib/jenkins', labels=''):
        """
        Create a new node in Jenkins.

        Args:
            name (str): Name of the new node.
            num_executors (int): Number of executors for the node (default is 2).
            node_description (str): Description of the node (default is None).
            remote_fs (str): Remote filesystem root directory (default is '/var/lib/jenkins').
            labels (str): Labels assigned to the node (default is '').

        Returns:
            bool: True if the node creation was successful, False otherwise.
        """
        return self.server.create_node(name, num_executors, node_description, remote_fs, labels)

    def enable_node(self, node_name):
        """
        Enable a node in Jenkins.

        Args:
            node_name (str): Name of the node to enable.

        Returns:
            bool: True if the node was enabled successfully, False otherwise.
        """
        return self.server.enable_node(node_name)

    def disable_node(self, node_name):
        """
        Disable a node in Jenkins.

        Args:
            node_name (str): Name of the node to disable.

        Returns:
            bool: True if the node was disabled successfully, False otherwise.
        """
        return self.server.disable_node(node_name)

    def get_all_nodes(self):
        """
        Get information about all nodes in the Jenkins environment.

        Returns:
            list: Information about all nodes.
        """
        return self.server.get_nodes()

    
