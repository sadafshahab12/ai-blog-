import React from "react";
import { Blog } from "../types/blog";
import Link from "next/link";

const BlogCard = ({ blog }: { blog: Blog }) => {
  return (
    <Link href={`/blog/${blog.id}`}>
      <div className="border p-5">
        <h1>{blog.title}</h1>
        <p>{blog.content}</p>
        <span>
          By {blog.author} - {new Date(blog.created_at).toLocaleDateString()}
        </span>
      </div>
    </Link>
  );
};

export default BlogCard;
