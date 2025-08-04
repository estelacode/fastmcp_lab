# FastMCP Lab
## Objetive
Create a mcp client that get access to tools, resources and prompts exposed by the created mcp server using the FastMCP framework.

# Initial Project Setup
1. Create Virtual Environment
```bash
py -3.13 -m venv .venv
```

2. Activate Virtual Environment
```bash
.venv\Scripts\activate
```

3. Install UV
```bash
pip install uv
uv --version
```

4. Create a new project with uv
```bash
uv init
```

5. Link my local repository to my Github remote repository
```bash
git remote add origin https://github.com/estelacode/fastmcp_lab.git
git remote -v
```

6. Add first commit and push the current branch and set the remote as upstream
```bash
git add README.md
git commit -m "First commit"
git push -u origin master
```

7. Install dependences
```bash
uv add fastmcp
```


## Git commands


```bash
# Displays the current state of the repository, including uncommitted changes and untracked files.
git status

# Adds all new and modified files in the current directory to the staging area.
git add .

# Adds a specific file to the staging area.
git add <file>

# Commits changes in the staging area and creates a new commit with the specified message.
git commit -m <message>

# Changes the commit message of the most recent commit.
git commit --amend -m "new message"

# Adds a new remote repository named "origin" and associates it with the specified Git repository URL.
git remote add origin https://github.com/user/repository_name.git

# Displays the list of configured remote repositories, including their names and URLs.
git remote -v

# Pushes local changes to the remote repository "origin" and sets the current branch as the upstream branch of the remote repository.
git push --upstream origin https://github.com/user/repository_name.git

# Pushes local changes to the remote repository "origin" and sets the "master" branch as the upstream branch of the remote repository.
git push -u origin master

# Downloads the latest changes from the remote repository.
git fetch origin

# Downloads the latest changes from the remote repository and merges them into the current branch.
git pull origin

# Merges the specified branch into the current branch.
git merge <branch_name>

# Creates a new branch named <new_branch_name> and switches to it.
git checkout -b <new_branch_name>

# Switches to an existing branch named <branch_name>.
git checkout <branch_name>

# Displays the list of local branches in the repository.
git branch

# Displays the list of remote branches in the repository.
git branch -r

# Deletes a local branch named <branch_name>.
git branch -d <branch_name>

# Deletes a remote branch named <branch_name> in the remote repository "origin".
git push origin --delete <branch_name>

# Changes the URL of the remote repository.
git remote set-url origin <new_url>

# Changes the URL of the remote repository.
git remote --set-url origin <new_url>

# Displays the commit history of the repository.
git log

# Displays the commit history of the repository in a more detailed format.
git log --graph --decorate --all

# Shows the difference between the current file and the file in the last commit.
git diff

# Shows the difference between the current file and the file in a specific commit.
git diff <commit_hash>

# Reverts changes made to the current file.
git checkout -- <file>

# Reverts changes made to all files.
git checkout -- .

# Deletes all untracked files in the current directory.
git clean -f
```