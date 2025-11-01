import Link from "next/link";

export default function Home() {
  return (
    <main>
      <Link href="/blog">Blog</Link>
      <Link href={"/blog/create"}>Create New Blog</Link>
    </main>
  );
}
