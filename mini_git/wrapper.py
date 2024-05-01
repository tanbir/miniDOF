import git
from git import GitCommandError

class GitWrapper:
    def __init__(self, repo_path):
        """
        Initializes the GitWrapper class with the path to the Git repository.

        Parameters:
        - repo_path (str): Path to the Git repository.
        """
        self.repo = git.Repo(repo_path)

    def get_branches(self):
        """
        Retrieves the list of branches in the repository.

        Returns:
        - List[str]: List of branch names.
        """
        return [str(branch) for branch in self.repo.branches]

    def get_tags(self):
        """
        Retrieves the list of tags in the repository.

        Returns:
        - List[str]: List of tag names.
        """
        return [str(tag) for tag in self.repo.tags]

    def get_current_branch(self):
        """
        Retrieves the name of the currently checked out branch.

        Returns:
        - str: Name of the current branch.
        """
        return str(self.repo.active_branch)

    def create_branch(self, branch_name, base_branch='master'):
        """
        Creates a new branch in the repository.

        Parameters:
        - branch_name (str): Name of the new branch.
        - base_branch (str): Name of the branch to base the new branch on. Defaults to 'master'.

        Returns:
        - bool: True if the branch creation was successful, False otherwise.
        """
        try:
            self.repo.create_head(branch_name, base=self.repo.head.reference)
            return True
        except GitCommandError:
            return False

    def delete_branch(self, branch_name):
        """
        Deletes a branch from the repository.

        Parameters:
        - branch_name (str): Name of the branch to delete.

        Returns:
        - bool: True if the branch deletion was successful, False otherwise.
        """
        try:
            self.repo.delete_head(branch_name)
            return True
        except GitCommandError:
            return False

    # Extension: More functionalities
    def get_commit(self, commit_id):
        """
        Retrieves information about a specific commit.

        Parameters:
        - commit_id (str): ID of the commit.

        Returns:
        - git.Commit: Commit object representing the specified commit.
        """
        return self.repo.commit(commit_id)

    def get_commits(self, branch='master', limit=None):
        """
        Retrieves a list of commit IDs for a given branch.

        Parameters:
        - branch (str): Name of the branch. Defaults to 'master'.
        - limit (int): Maximum number of commits to retrieve. Defaults to None (no limit).

        Returns:
        - List[str]: List of commit IDs.
        """
        commits = self.repo.iter_commits(branch, max_count=limit)
        return [commit.hexsha for commit in commits]

    def commit_changes(self, message):
        """
        Commits changes to the repository.

        Parameters:
        - message (str): Commit message.
        """
        self.repo.index.commit(message)

    def push_changes(self, remote_name='origin', branch_name='master'):
        """
        Pushes changes to a remote repository.

        Parameters:
        - remote_name (str): Name of the remote repository. Defaults to 'origin'.
        - branch_name (str): Name of the branch to push. Defaults to 'master'.

        Returns:
        - bool: True if the push was successful, False otherwise.
        """
        try:
            self.repo.remote(name=remote_name).push(refspec=f'refs/heads/{branch_name}')
            return True
        except GitCommandError:
            return False

    def pull_changes(self, remote_name='origin', branch_name='master'):
        """
        Pulls changes from a remote repository.

        Parameters:
        - remote_name (str): Name of the remote repository. Defaults to 'origin'.
        - branch_name (str): Name of the branch to pull. Defaults to 'master'.

        Returns:
        - bool: True if the pull was successful, False otherwise.
        """
        try:
            self.repo.remote(name=remote_name).pull(branch_name)
            return True
        except GitCommandError:
            return False

    def fetch(self, remote_name='origin'):
        """
        Fetches changes from a remote repository.

        Parameters:
        - remote_name (str): Name of the remote repository. Defaults to 'origin'.

        Returns:
        - bool: True if the fetch was successful, False otherwise.
        """
        try:
            self.repo.remote(name=remote_name).fetch()
            return True
        except GitCommandError:
            return False

    def merge(self, branch_name, message=None):
        """
        Merges changes from another branch into the current branch.

        Parameters:
        - branch_name (str): Name of the branch to merge.
        - message (str): Merge commit message.

        Returns:
        - bool: True if the merge was successful, False otherwise.
        """
        try:
            self.repo.git.merge(branch_name, message=message)
            return True
        except GitCommandError:
            return False

    def reset_hard(self, commit_id='HEAD'):
        """
        Resets the working directory to a specific commit.

        Parameters:
        - commit_id (str): ID of the commit to reset to. Defaults to 'HEAD'.

        Returns:
        - bool: True if the reset was successful, False otherwise.
        """
        try:
            self.repo.head.reset(commit_id, index=True, working_tree=True)
            return True
        except GitCommandError:
            return False

    def add_remote(self, name, url):
        """
        Adds a new remote repository.

        Parameters:
        - name (str): Name of the remote.
        - url (str): URL of the remote repository.

        Returns:
        - bool: True if the remote was added successfully, False otherwise.
        """
        try:
            self.repo.create_remote(name, url)
            return True
        except GitCommandError:
            return False

    def remove_remote(self, name):
        """
        Removes an existing remote repository.

        Parameters:
        - name (str): Name of the remote to remove.

        Returns:
        - bool: True if the remote was removed successfully, False otherwise.
        """
        try:
            self.repo.delete_remote(name)
            return True
        except GitCommandError:
            return False

    def get_diff(self, ref_a='HEAD', ref_b=None):
        """
        Retrieves the difference between two references.

        Parameters:
        - ref_a (str): First reference. Defaults to 'HEAD'.
        - ref_b (str): Second reference. Defaults to None.

        Returns:
        - str: Difference between the references.
        """
        diff = self.repo.git.diff(ref_a, ref_b)
        return diff

    def add_files(self, file_paths):
        """
        Adds files to the index for staging.

        Parameters:
        - file_paths (List[str]): List of file paths to add.
        """
        self.repo.index.add(file_paths)

    def checkout(self, ref):
        """
        Checks out a specific reference.

        Parameters:
        - ref (str): Reference to check out.

        Returns:
        - bool: True if the checkout was successful, False otherwise.
        """
        try:
            self.repo.git.checkout(ref)
            return True
        except GitCommandError:
            return False

    def clone(self, repo_url, dest_path):
        """
        Clones a remote repository to the specified destination path.

        Parameters:
        - repo_url (str): URL of the remote repository.
        - dest_path (str): Destination path to clone the repository to.

        Returns:
        - bool: True if the clone was successful, False otherwise.
        """
        try:
            git.Repo.clone_from(repo_url, dest_path)
            return True
        except GitCommandError:
            return False

    def blame(self, file_path):
        """
        Retrieves blame information for a specific file.

        Parameters:
        - file_path (str): Path of the file to retrieve blame information for.

        Returns:
        - str: Blame information.
        """
        blame_info = self.repo.git.blame(file_path)
        return blame_info

    def get_status(self):
        """
        Retrieves the status of the repository.

        Returns:
        - str: Status of the repository.
        """
        return self.repo.git.status()

    def get_remote_url(self, remote_name='origin'):
        """
        Retrieves the URL of a remote repository.

        Parameters:
        - remote_name (str): Name of the remote repository. Defaults to 'origin'.

        Returns:
        - str: URL of the remote repository.
        """
        return self.repo.remote(name=remote_name).url

    def rename_branch(self, old_name, new_name):
        """
        Renames a branch.

        Parameters:
        - old_name (str): Current name of the branch.
        - new_name (str): New name for the branch.

        Returns:
        - bool: True if the branch was renamed successfully, False otherwise.
        """
        try:
            self.repo.git.branch('-m', old_name, new_name)
            return True
        except GitCommandError:
            return False

    def stash_changes(self):
        """
        Stashes changes in the repository.

        Returns:
        - bool: True if the stash was successful, False otherwise.
        """
        try:
            self.repo.git.stash()
            return True
        except GitCommandError:
            return False

    def apply_stash(self):
        """
        Applies the latest stash to the working directory.

        Returns:
        - bool: True if the stash was applied successfully, False otherwise.
        """
        try:
            self.repo.git.stash('apply')
            return True
        except GitCommandError:
            return False
