backend virtual environment
uv venv
source .venv/Scripts/activate
pip install fastapi uvicorn pydantic
_uv pip install "fastapi[standard]"_
fastapi dev main.py

1. Remove the submodule reference

In your main repo folder:

git rm -r --cached frontend

2. Delete the .git inside the frontend folder

If you’re on Git Bash:

rm -rf frontend/.git

Or on Windows CMD:

rmdir /s /q frontend\.git

3. Add and commit again
   git add .
   git commit -m "Fixed frontend folder — removed submodule"
   git push -u origin main
