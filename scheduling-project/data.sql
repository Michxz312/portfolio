CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_level VARCHAR(50),
    training TEXT,
    salary FLOAT
);

CREATE TABLE customer (
    day_label VARCHAR(50),
    shift VARCHAR(50),
    shift_demand FLOAT
);