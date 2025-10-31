import React from "react";
import { Blog } from "../types/blog";

const BlogCard = ({ blog }: { blog: Blog }) => {
  return (
    <div>
      <h1>{blog.title}</h1>
      <p>{blog.content}</p>
      <span>
        By {blog.author} - {new Date(blog.created_at).toLocaleDateString()}
      </span>
    </div>
  );
};

export default BlogCard;
