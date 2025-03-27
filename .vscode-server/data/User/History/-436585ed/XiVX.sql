-- create table with id default 1 and unique.
CREATE TABLE IF NOT EXISTS unique_id (
    id IF NOT EXISTS INT DEFAULT 1,
    name VARCHAR(256)
);
