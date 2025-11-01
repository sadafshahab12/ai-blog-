from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Blog
from datetime import datetime
import os

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

DATA_FILE = "blogs.json"


@app.get("/blogs")
def get_blogs():
    return blogs


@app.get("/blogs/{blog_id}")
def get_single_blog(blog_id: int):
    for blog in blogs:
        if blog.id == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")
