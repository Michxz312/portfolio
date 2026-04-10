CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_level VARCHAR(50),
    training TEXT,
    salary FLOAT
);

CREATE TABLE customers (
    day_label VARCHAR(50),
    shift VARCHAR(50),
    shift_demand FLOAT
);