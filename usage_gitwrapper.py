from gitwrapper.gitwrapper import GitWrapper

# Instantiate the GitWrapper class
wrapper = GitWrapper('/path/to/your/repo')

# Get the list of branches
branches = wrapper.get_branches()
print("Branches:", branches)

# Get the list of commits in the master branch
commits = wrapper.get_commits(branch=branches[0], limit=5)
print("Commits:", commits)

tags = wrapper.get_tags()
print("Tags:", tags)

current_branch = wrapper.get_current_branch()
print("Current branch:", current_branch)