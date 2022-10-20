import { Button, IconButton, Input, useColorMode } from "@chakra-ui/react";
import { useRouter } from "next/router";
import { NextPage } from "next/types";
import { useState } from "react";
import { RiMoonFill, RiSunLine } from "react-icons/ri";
import excuteQuery from "../lib/db.js"

type Post = {
  id: string;
  title: string;
  content: string;
};

export default function HomePage() {
  const router = useRouter();
  const posts: Post[] = [
    {
      id: "post1",
      title: "This one weird trick makes using databases fun",
      content: "Use EdgeDB",
    },
    {
      id: "post2",
      title: "How to build a blog with EdgeDB and Next.js",
      content: "Let's start by scaffolding our app...",
    },
  ];

  //const [posts, setPosts] = useState<Post[] | null>(null);
  //    useEffect(() => {
  //      fetch(`/api/post`)
  //        .then((result) => result.json())
  //        .then(setPosts);
  //    }, []);
  if (!posts)
    return <p>Loading...</p>;

  const { colorMode, toggleColorMode } = useColorMode();

  const [value, setValue] = useState("");
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  // const queryDB = async () => {
  //   try {
  //     const result = await excuteQuery({
  //       query: 'SELECT * FROM users WHERE email = ?',
  //       values: [],
  //     });
  //     console.log(result);
  //   } catch (error) {
  //     console.log(error);
  //   }
  // }

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch('api/mysql', { method: "GET" });
    router.push(`recipe/${value}`);
    // Do work on this string
    //location.assign("http://www.mozilla.org");
  };

  return (
    <>
      <IconButton
        aria-label="theme toggle"
        icon={colorMode === "light" ? <RiMoonFill /> : <RiSunLine />}
        onClick={toggleColorMode} />
      <form onSubmit={handleSubmit}>
        <Input
          placeholder={"Search"}
          onChange={handleChange}
          onSubmit={handleSubmit}
          required />
        <Button type="submit">Search</Button>
      </form>
    </>
  );
}