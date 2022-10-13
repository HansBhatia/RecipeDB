import { NextPage } from 'next/types';
import { useState, useEffect } from 'react';
import { Container, Input, Row, Image, Spacer } from "@nextui-org/react";

type Post = {
  id: string;
  title: string;
  content: string;
};

const HomePage: NextPage = () => {
  const posts: Post[] = [
    {
      id: 'post1',
      title: 'This one weird trick makes using databases fun',
      content: 'Use EdgeDB',
    },
    {
      id: 'post2',
      title: 'How to build a blog with EdgeDB and Next.js',
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

  return (<>
    <Container alignItems="center" justify='center' wrap='wrap' fluid responsive>
      <Image
        width={320}
        height={180}
        src="https://github.com/nextui-org/nextui/blob/next/apps/docs/public/nextui-banner.jpeg?raw=true"
        alt="Default Image"
        objectFit="cover"
      />
      <Spacer y={2} />
      <Row justify="center" align="center">
        <Input
          clearable
          css={{
            margin: 'auto',
            w: "50%",
            "@xsMax": {
              mw: "300px",
            },
          }}
          placeholder="Search..."
        />
      </Row>
    </Container>
  </>)
  {/* {posts.map((post) => {
      return (<>
        <a href={`/post/${post.id}`} key={post.id}>
          <div>
            <p>{post.title}</p>
          </div>
        </a>
      </>
      );
    })} */}
}

export default HomePage;