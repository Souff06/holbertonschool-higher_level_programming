-- create table with id default 1 and unique.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 unique,
    name VARCHAR(256)
);
