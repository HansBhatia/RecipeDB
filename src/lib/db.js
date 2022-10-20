import mysql from 'serverless-mysql';
const db = mysql({
  config: {
    host: '165.232.138.171',
    port: 3306,
    database: 'main',
    user: 'recipeApp',
    password: 'cS348!project'
  }
});
// const db = mysql({
//   config: {
//     host: process.env.MYSQL_HOST,
//     port: process.env.MYSQL_PORT,
//     database: process.env.MYSQL_DATABASE,
//     user: process.env.MYSQL_USER,
//     password: process.env.MYSQL_PASSWORD
//   }
// });

export default async function excuteQuery({ query, values }) {
  try {
    const results = await db.query(query, values);
    await db.end();
    return results;
  } catch (error) {
    return { error };
  }
}