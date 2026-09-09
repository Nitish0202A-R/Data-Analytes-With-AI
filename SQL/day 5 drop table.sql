CREATE TABLE employee2(
    employee_id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	Postition VARCHAR(50),
	Departmant VARCHAR(50),
	datE_hring DATE,
	Salary NUMERIC(10,2)

);

SELECT *FROM employee2;

INSERT INTO employee2
(employee_id, name, postiion, departmant, datE_hring, salary)
VALUES
(140, 'Nitish Kumar', 'Software', 'IT', '2025-10-15', 45000.00),
(150, 'Rohit Kumar', 'Data Analyst', 'IT', '2025-11-17', 50000.00),
(160, 'Ravi Kumar', 'Computer repair', 'IT', '2025-10-01', 60000.00),
(170, 'Aarti Kumar', 'Doctor', 'marahian', '2025-10-06', 70000.00),
(180, 'Abhiya Kumar', 'Student', 'Techar', '2025-10-02', 40000.00);

DELETE FROM employee2
WHERE employee_id = 180;

ALTER TABLE employee2
DROP COLUMN salary;

DROP TABLE IF EXISTS employee3;
DROP TABLE IF EXISTS company2;


--Drop the table if it already exists
DROP TABLE IF EXISTS users;


--Create the users table
CREATE TABLE IF NOT EXISTS users(
User_id INT PRIMARY KEY,
Name VARCHAR(50),
Email VARCHAR(100)UNIQUE,
Age INTEGER CHECK(Age>=18),
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);


SELECT * FROM users;

INSERT INTO users(User_id,Name,Email,Age,)
VALUES
(2,'Aarit Kumar','aarit1@gmail.com',23,),
(101,'Rohit Kumar','rohit13@gmail.com',21,),
(102,'Ravi Kumar','ravi1@gmail.com',20,);


-- INSERTING DATA INTO TABLE
INSERT INTO users(User_id,Name,Email,Age,)
VALUES
(1,'Nitish Kumar','nitish12@gmail.com',24,),


CREATE TABLE users(
    User_id INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Age INTEGER CHECK(Age >= 18),
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    City VARCHAR(50)
);


--Insert 5 Sample Users into The Users table
INSERT INTO users(User_id, Name, Email, Age, City)
VALUES
(1,'Nitish Kumar','nitish12@gmail.com',24,'Patna'),
(2, 'Aarit Kumar', 'aarit1@gmail.com', 23, 'Bihar'),
(101, 'Rohit Kumar', 'rohit13@gmail.com', 21, 'Saran'),
(102, 'Ravi Kumar', 'ravi1@gmail.com', 20, 'Chapra');


SELECT * FROM users;

-- only choose show the data values

SELECT user_id,city FROM users;

-- Data Update
UPDATE users
SET age=25
WHERE name='Nitish Kumar'


UPDATE users
SET city='chapra'
WHERE name='Rohit Kumar'


UPDATE users
SET city='saran'
WHERE age>=20;


UPDATE users
SET city='Bihar',age=24
WHERE name='Nitish Kumar';

UPDATE users
SET age=age+1
WHERE email LIKE 'nitish12@gmail.com'


UPDATE users
SET age=age+1
WHERE email LIKE '%@gmail.com'

-- How to arange order
SELECT * FROM users ORDER BY user_id ASC;



