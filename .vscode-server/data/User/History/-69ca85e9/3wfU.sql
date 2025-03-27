-- create table with id default 1 and unique.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL PRIMARY,
    name VARCHAR(256) NOT NULL
);
