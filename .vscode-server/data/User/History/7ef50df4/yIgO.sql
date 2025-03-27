-- lists all privileges of the MySQL users user_0d_1 and user_0d_2.
CREATE USER IF NOT EXISTS user_0d_1 (
    id INT PRIMARY KEY user_0d_1_pwd,
    name VARVHAR(100)
);
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
