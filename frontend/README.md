backend virtual environment 
uv venv
source .venv/Scripts/activate
pip install fastapi uvicorn pydantic
*uv pip install "fastapi[standard]"*
fastapi dev main.py