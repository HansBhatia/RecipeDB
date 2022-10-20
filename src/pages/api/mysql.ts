// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import excuteQuery from '../../lib/db'

type Data = {
  name: string
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const payload = req.body as {
    score: string
  }
  if (req.method == "GET") {
    try {
          const result = await excuteQuery({
            query: 'SHOW TABLES;',
            values: [],
          });
          console.log(result);
          return res.status(200)
        } catch (error) {
          console.log(error);
          return res.status(300)
        }
  }
}
