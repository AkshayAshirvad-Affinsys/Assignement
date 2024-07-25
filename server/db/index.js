const fs = require('fs');
const { Pool } = require('pg');

// Read secrets from files
const pgUser = fs.readFileSync('/run/secrets/user', 'utf8').trim();
const pgPassword = fs.readFileSync('/run/secrets/password', 'utf8').trim();
const pgDatabase = fs.readFileSync('/run/secrets/database', 'utf8').trim();

const pool = new Pool({
  user: pgUser,
  host: process.env.PGHOST || 'localhost',
  database: pgDatabase,
  password: pgPassword,
  port: process.env.PGPORT || 5432,
});

module.exports = {
  query: (text, params) => pool.query(text, params),
};


