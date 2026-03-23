CREATE DATABASE college;

USE college;

CREATE TABLE student (
	rollno INT,
    name VARCHAR(30),
    age INT
);

INSERT INTO student 
VALUES
(101, "adam", 12),
(102, "bob", 14);

SELECT * FROM student;

SHOW DATABASES;

CREATE DATABASE adoni;

USE adoni;

CREATE TABLE user (
	id INT, 
    age INT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT,
    CONSTRAINT CHECK (age >= 13),
    PRIMARY KEY (id)
);

CREATE TABLE post (
	id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 18, "riya", "riya@gmail.com", 234, 156),
(3, 21, "arjun", "arjun@outlook.com", 345, 167),
(4, 25, "meera", "meera@hotmail.com", 456, 178);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(5, 30, "sahil", "sahil@gmail.com", 567, 189),
(6, 27, "kavya", "kavya@yahoo.com", 678, 192);

RENAME TABLE user TO players;

SELECT id, name, email FROM players;

SELECT * FROM players;

SELECT DISTINCT age FROM players;

SELECT * FROM players WHERE followers >= 200;

SELECT name, age FROM players WHERE followers >= 200;

SELECT name, age, followers FROM players WHERE age > 15 AND followers > 200;

SELECT name, age, followers FROM players WHERE age > 15 OR followers > 200;

SELECT name, age, followers FROM players WHERE age BETWEEN 15 AND 17;

SELECT name, age, followers FROM players WHERE email IN ("adam@yahoo.in", "riya@gmail.com", "abc@gmail.com")

SELECT name, age, followers FROM players WHERE age IN (14, 16);

SELECT name, age, followers FROM players WHERE age NOT IN (14, 16);

SELECT * FROM players WHERE followers >= 200 LIMIT 2;

SELECT name, age, followers FROM players ORDER BY followers ASC;

SELECT name, age, followers FROM players ORDER BY followers DESC;

SELECT COUNT(age) FROM players WHERE age = 14;

SELECT SUM(followers) FROM players;

SELECT AVG(price) FROM players;

SELECT MIN(age) FROM players;

SELECT MAX(age) FROM players;

SELECT count(id) FROM players GROUP BY age;

SELECT AGE, MAX(followers) FROM players GROUP BY age HAVING max(followers) > 200;

SET SQL_SAFE_UPDATES = 0;

UPDATE players SET followers = 600 WHERE age = 16;

DELETE FROM players WHERE age = 14;

ALTER TABLE players ADD COLUMN area VARCHAR(20);

ALTER TABLE players DROP COLUMN area;

ALTER TABLE players ADD COLUMN area VARCHAR(20);
