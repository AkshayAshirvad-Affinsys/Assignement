
/*CREATE DATABASE yelp;


CREATE USER postgres WITH PASSWORD 'password123';


GRANT ALL PRIVILEGES ON DATABASE yelp TO postgres;


\c yelp



CREATE TABLE IF NOT EXISTS restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    rating NUMERIC,
    location VARCHAR(255),
    price_range VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS reviews (
    id BIGSERIAL PRIMARY KEY,
    restaurant_id BIGINT NOT NULL,
    name VARCHAR(50) NOT NULL,
    review TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
);






select *
from restaurants
    left join(
        select restaurant_id,
            count(*),
            TRUNC(AVG(rating, 1)) as average_rating
        from reviews
        group by restaurant_id
    ) reviews on restaurants.id = reviews.restaurant_id;*/

 -- Check if the database exists before creating it
DO $$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database
      WHERE datname = 'yelp') THEN
      CREATE DATABASE yelp;
   END IF;
END
$$;


\c yelp;


DO $$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_roles
      WHERE rolname = 'postgres') THEN
      CREATE USER postgres WITH PASSWORD 'password123';
   END IF;
END
$$;


GRANT ALL PRIVILEGES ON DATABASE yelp TO postgres;


CREATE TABLE IF NOT EXISTS restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    rating NUMERIC,
    location VARCHAR(255),
    price_range VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS reviews (
    id BIGSERIAL PRIMARY KEY,
    restaurant_id BIGINT NOT NULL,
    name VARCHAR(50) NOT NULL,
    review TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
);


SELECT *
FROM restaurants
LEFT JOIN (
    SELECT restaurant_id,
           COUNT(*) AS review_count,
           TRUNC(AVG(rating), 1) AS average_rating
    FROM reviews
    GROUP BY restaurant_id
) reviews ON restaurants.id = reviews.restaurant_id;
   