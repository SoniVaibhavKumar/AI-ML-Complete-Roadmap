CREATE DATABASE IF NOT EXISTS colleges;

USE colleges;

CREATE TABLE Teacher(
	id INT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(100),
    salary int
);

INSERT INTO Teacher (id, name, subject, salary) VALUES
(23, "ajay", "math", 50000),
(47, "bharat", "english", 60000),
(18, "chetan", "chemistry", 45000),
(0, "divya", "physics", 75000);

SELECT * FROM Teacher;

SELECT * FROM Teacher WHERE salary > 55000;

ALTER TABLE Teacher CHANGE COLUMN salary ctc INT;

SET SQL_SAFE_UPDATES = 0;

UPDATE Teacher SET ctc = ctc + ctc * 0.25;

ALTER TABLE Teacher ADD COLUMN city VARCHAR(50) DEFAULT "Durgapur"

ALTER TABLE Teacher DROP COLUMN ctc;

 CREATE TABLE student (
	rollno INT PRIMARY KEY,
    name VARCHAR(30),
    city VARCHAR(30),
    marks INT
);

INSERT INTO student (rollno, name, city, marks) VALUES
(110, "adam", "Delhi", 76),
(108, "bob", "Mumbai", 65),
(124, "casey", "Pune", 94),
(112, "duke", "Pune", 80);

SELECT * FROM student;

SELECT DISTINCT city FROM student;

SELECT city, max(marks) FROM student GROUP BY city;

SELECT avg(marks) FROM student;

ALTER TABLE student ADD COLUMN grade VARCHAR(2);

UPDATE student SET grade = "O" WHERE marks >= 80;

UPDATE student SET grade = "A" WHERE marks >= 70 AND marks < 80;

UPDATE student SET grade = "B" WHERE marks >= 60 AND marks < 70