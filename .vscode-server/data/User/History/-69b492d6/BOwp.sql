-- lists all privileges of the MySQL users user_0d_1 and user_0d_2.
CREATE DATABASE if not EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT, INSERT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
