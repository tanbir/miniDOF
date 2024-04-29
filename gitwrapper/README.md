# GitWrapper Class Documentation

The GitWrapper class provides a convenient wrapper for interacting with Git repositories using the GitPython library.

## Installation

Install GitPython using pip:

```bash
pip install gitpython
```

## Usage

```python
from git_wrapper import GitWrapper

# Create an instance of the GitWrapper class
git_wrapper = GitWrapper('/path/to/your/repo')

# Use GitWrapper methods to interact with Git repositories
```

## GitWrapper Functions

| Function Name          | Description                                             | Inputs                            | Outputs                           |
|------------------------|---------------------------------------------------------|-----------------------------------|-----------------------------------|
| `__init__`             | Initializes the GitWrapper instance                     | repo_path (str)                   | None                              |
| `clone`                | Clones a Git repository                                 | repo_url (str), destination (str) | None                              |
| `add`                  | Adds file(s) to the Git index                           | file_paths (list)                 | None                              |
| `commit`               | Commits changes to the Git repository                    | message (str)                     | None                              |
| `push`                 | Pushes changes to the remote Git repository              | remote_name (str), branch_name (str) | None                              |
| `pull`                 | Pulls changes from the remote Git repository            | remote_name (str), branch_name (str) | None                              |
| `checkout`             | Checks out a branch or file in the Git repository       | target (str)                      | None                              |
| `status`               | Retrieves the status of the Git repository               | None                              | Git status as a dictionary       |
| `diff`                 | Retrieves the diff of the Git repository                 | None                              | Git diff as a string             |
| `log`                  | Retrieves the commit history of the Git repository       | None                              | Git log as a list of dictionaries|
| `branch`               | Retrieves information about branches in the Git repository | None                            | List of branch names             |
| `merge`                | Merges a branch into the current branch                 | branch_name (str)                 | None                              |
| `tag`                  | Creates a tag for the current commit                     | tag_name (str)                    | None                              |
| `remote`               | Retrieves information about remote repositories         | None                              | List of remote names             |
| `fetch`                | Fetches changes from a remote repository                | remote_name (str)                 | None                              |
| `rename_branch`        | Renames a branch in the Git repository                  | old_name (str), new_name (str)    | None                              |
| `stash_changes`        | Stashes changes in the Git repository                   | None                              | None                              |
| `apply_stash`          | Applies stashed changes to the Git repository           | stash_index (int)                 | None                              |
| `blame`                | Retrieves blame information for a file in the Git repository | file_path (str)                | Blame information as a dictionary|
| `get_status`           | Retrieves the status of specific files in the Git repository | file_paths (list)             | Status of files as a dictionary  |
| `get_remote_url`       | Retrieves the URL of the remote repository              | remote_name (str)                 | URL of the remote repository     |
