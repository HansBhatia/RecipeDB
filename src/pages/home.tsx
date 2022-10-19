import { Button, IconButton, Input, useColorMode } from "@chakra-ui/react";
import { useRouter } from "next/router";
import { NextPage } from "next/types";
import { useState } from "react";
import { RiMoonFill, RiSunLine } from "react-icons/ri";

type Post = {
  id: string;
  title: string;
  content: string;
};

const HomePage: NextPage = () => {
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
  if (!posts) return <p>Loading...</p>;

  const { colorMode, toggleColorMode } = useColorMode();

  const [value, setValue] = useState("");
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(value);
    router.push(`recipe/${value}`);
    // Do work on this string
    //location.assign("http://www.mozilla.org");
  };
  return (
    <>
      <IconButton
        aria-label="theme toggle"
        icon={colorMode === "light" ? <RiMoonFill /> : <RiSunLine />}
        onClick={toggleColorMode}
      />
      <form onSubmit={handleSubmit}>
        <Input
          placeholder={"Search"}
          onChange={handleChange}
          onSubmit={handleSubmit}
          required
        />
        <Button type="submit">Search</Button>
      </form>
    </>
  );
};

export default HomePage;
