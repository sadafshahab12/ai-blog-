"use client";
import { useParams } from "next/navigation";
import React, { useEffect, useState } from "react";
interface Blog {
  id: number;
  title: string;
  content: string;
  author: string;
  created_at: string;
}
const SingleBlogPage = () => {
  const { slug } = useParams(); // it grabs slug from url
  const [blog, setBlog] = useState<Blog | null>(null);
  useEffect(() => {
    if (slug) {
      fetch(`http://127.0.0.1:8000/blogs/${slug}`)
        .then((res) => res.json())
        .then((data) => setBlog(data));
    }
  }, [slug]);

  if (!blog) return <p>Loading...</p>;
  return (
    <main>
      <h1>{blog.title}</h1>
      <p>
        {blog.author} - {new Date(blog.created_at).toLocaleDateString()}
      </p>
      <article>{blog.content}</article>
    </main>
  );
};

export default SingleBlogPage;
