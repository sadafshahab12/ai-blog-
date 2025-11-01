from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Blog
from datetime import datetime
import os, json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# blogs = [
#     Blog(
#         id=1,
#         title="First Blog",
#         content="Hello world!",
#         author="Sadaf",
#         created_at=datetime.now(),
#     ),
#     Blog(
#         id=2,
#         title="AI Blog",
#         content="Let’s build something awesome.",
#         author="Sadaf",
#         created_at=datetime.now(),
#     ),
# ]

DATA_FILE = "blogs.json"


def load_blogs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_blogs(blogs):
    with open(DATA_FILE, "w") as f:
        json.dump(blogs, f, indent=4, default=str)


@app.get("/blogs")
def get_blogs():
    blogs = load_blogs()
    return blogs


@app.get("/blogs/{blog_id}")
def get_single_blog(blog_id: int):
    blogs = load_blogs()
    for blog in blogs:
        if blog["id"] == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")


@app.post("/blogs")
def create_blog(blog: Blog):
    blogs = load_blogs()
    blog_dict = blog.model_dump()
    blog_dict["id"] = len(blogs) + 1
    blog_dict["created_at"] = datetime.now()
    blogs.append(blog_dict)
    save_blogs(blogs)
    return {"message": "Blog created successfully", "blog": blog}


@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):
    blogs = load_blogs()

    # find the blog to delete
    for blog in blogs:
        if blog["id"] == blog_id:
            blogs.remove(blog)
            save_blogs(blogs)
            return {"message": f"Blog with id {blog_id} deleted successfully."}
    raise HTTPException(status_code=404, detail="Blog not found")
