CREATE TABLE employee(
    employee_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	Postiion VARCHAR(50),
	Departmant VARCHAR(50),
	datE_hring DATE,
	Salary NUMERIC(10,2)

);

SELECT *FROM employee;