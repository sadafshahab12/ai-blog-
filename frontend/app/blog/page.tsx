"use client";
import React, { useEffect, useState } from "react";
import { Blog } from "../types/blog";
import BlogCard from "../components/BlogCard";

const BlogPage = () => {
  const [blogs, setBlogs] = useState<Blog[]>([]);
  
  useEffect(() => {
    fetch("http://127.0.0.1:8000/blogs")
      .then((res) => res.json())
      .then((data) => setBlogs(data));
  }, []);
  return (
    <main>
      <h1>My Blogs</h1>
      <div>
        {blogs.map((blog) => (
          <BlogCard key={blog.id} blog={blog} />
        ))}
      </div>
    </main>
  );
};

export default BlogPage;
