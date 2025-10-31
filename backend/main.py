from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Blog
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
blogs = [
    Blog(
        id=1,
        title="First Blog",
        content="Hello world!",
        author="Sadaf",
        created_at=datetime.now(),
    ),
    Blog(
        id=2,
        title="AI Blog",
        content="Let’s build something awesome.",
        author="Sadaf",
        created_at=datetime.now(),
    ),
]


@app.get("/blogs")
def get_blogs():
    return blogs
