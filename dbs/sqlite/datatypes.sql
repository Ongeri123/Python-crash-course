CREATE TABLE IF NOT EXISTS student(
    id SERIAL,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--INSERT INTO student(name, email, dob, phone, marks, created_at, updated_at)
--VALUES ('John Doe', 'john.doe@example.com', '1990-01-01', 1234567890, 85.5, '2023-04-15 10:00:00', '2023-04-15 10:00:00');

--SELECT * FROM student;