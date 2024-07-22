/*const { Pool } = require("pg");

const pool = new Pool();
module.exports = {
  query: (text, params) => pool.query(text, params),
};*/

const { Pool } = require('pg');
const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  port: process.env.DB_PORT || 5432,
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'password123',
  database: process.env.DB_NAME || 'yelp'
});

