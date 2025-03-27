-- create table with id default 1 and unique.
CREATE TABLE IF NOT EXISTS id_not_null (
    id IF NOT EXISTS INT DEFAULT 1,
    name VARCHAR(256)
);