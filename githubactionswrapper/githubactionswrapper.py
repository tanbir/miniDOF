import requests
import json

class GitHubActionsWrapper:
    def __init__(self, repo_owner, repo_name, personal_access_token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.headers = {
            "Authorization": f"token {personal_access_token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def trigger_workflow(self, workflow_file_path, ref="main", inputs=None):
        """
        Trigger a GitHub Actions workflow.

        Args:
            workflow_file_path (str): Path to the workflow YAML file.
            ref (str, optional): The branch or tag name. Defaults to "main".
            inputs (dict, optional): Input parameters for the workflow. Defaults to None.

        Returns:
            str: The ID of the created workflow run.
        """
        url = f"{self.base_url}/actions/workflows/{workflow_file_path}/dispatches"
        payload = {"ref": ref, "inputs": inputs}
        response = requests.post(url, headers=self.headers, json=payload)
        if response.status_code == 204:
            return "Workflow triggered successfully."
        else:
            return f"Failed to trigger workflow: {response.text}"

    def get_workflow_runs(self, workflow_id):
        """
        Get all workflow runs for a specific workflow.

        Args:
            workflow_id (str): The ID of the workflow.

        Returns:
            list: List of dictionaries containing information about each workflow run.
        """
        url = f"{self.base_url}/actions/workflows/{workflow_id}/runs"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()["workflow_runs"]
        else:
            return []

    def get_workflow_run_logs(self, run_id):
        """
        Get the logs for a specific workflow run.

        Args:
            run_id (str): The ID of the workflow run.

        Returns:
            str: The logs for the workflow run.
        """
        url = f"{self.base_url}/actions/runs/{run_id}/logs"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to get logs for run {run_id}: {response.text}"

    def get_workflow_job_logs(self, run_id, job_name):
        """
        Get the logs for a specific job within a workflow run.

        Args:
            run_id (str): The ID of the workflow run.
            job_name (str): The name of the job.

        Returns:
            str: The logs for the job.
        """
        url = f"{self.base_url}/actions/jobs/{job_name}/logs"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to get logs for job {job_name} in run {run_id}: {response.text}"

    def get_artifacts_for_run(self, run_id):
        """
        Get the artifacts produced by a specific workflow run.

        Args:
            run_id (str): The ID of the workflow run.

        Returns:
            list: List of artifacts.
        """
        url = f"{self.base_url}/actions/runs/{run_id}/artifacts"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()["artifacts"]
        else:
            return []

    def download_artifact(self, artifact_id, destination):
        """
        Download a specific artifact from a workflow run.

        Args:
            artifact_id (str): The ID of the artifact.
            destination (str): The path to save the artifact.

        Returns:
            str: Path to the downloaded artifact.
        """
        url = f"{self.base_url}/actions/artifacts/{artifact_id}/zip"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            with open(destination, "wb") as f:
                f.write(response.content)
            return destination
        else:
            return f"Failed to download artifact {artifact_id}: {response.text}"

    def get_workflow_id(self, workflow_file_path):
        """
        Get the ID of a workflow using its file path.

        Args:
            workflow_file_path (str): Path to the workflow YAML file.

        Returns:
            str: The ID of the workflow.
        """
        url = f"{self.base_url}/actions/workflows"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            workflows = response.json()["workflows"]
            for workflow in workflows:
                if workflow["path"] == workflow_file_path:
                    return workflow["id"]
            return None
        else:
            return None

    def cancel_workflow_run(self, run_id):
        """
        Cancel a specific workflow run.

        Args:
            run_id (str): The ID of the workflow run to cancel.

        Returns:
            str: Confirmation message.
        """
        url = f"{self.base_url}/actions/runs/{run_id}/cancel"
        response = requests.post(url, headers=self.headers)
        if response.status_code == 202:
            return f"Workflow run {run_id} has been canceled."
        else:
            return f"Failed to cancel workflow run {run_id}: {response.text}"

    def rerun_workflow(self, run_id):
        """
        Rerun a specific workflow.

        Args:
            run_id (str): The ID of the workflow run to rerun.

        Returns:
            str: Confirmation message.
        """
        url = f"{self.base_url}/actions/runs/{run_id}/rerun"
        response = requests.post(url, headers=self.headers)
        if response.status_code == 201:
            return f"Workflow {run_id} has been rerun."
        else:
            return f"Failed to rerun workflow {run_id}: {response.text}"

    def get_workflow_run_jobs(self, run_id):
        """
        Get the jobs for a specific workflow run.

        Args:
            run_id (str): The ID of the workflow run.

        Returns:
            list: List of dictionaries containing information about each job.
        """
        url = f"{self.base_url}/actions/runs/{run_id}/jobs"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()["jobs"]
        else:
            return []

    def get_job_logs(self, run_id, job_id):
        """
        Get the logs for a specific job within a workflow run.

        Args:
            run_id (str): The ID of the workflow run.
            job_id (str): The ID of the job.

        Returns:
            str: The logs for the job.
        """
        url = f"{self.base_url}/actions/jobs/{job_id}/logs"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to get logs for job {job_id} in run {run_id}: {response.text}"
