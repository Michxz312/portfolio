use mydb;

CREATE TABLE students (
    id INT PRIMARY KEY,
    gender INT,
    international INT,
    preference TEXT
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    max INT
); 