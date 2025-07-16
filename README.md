# FastMCP Lab



# Installation
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
git commit -m "First Commit"
git push -u origin master
```

7. Install dependences
```bash
uv add fastmcp
```