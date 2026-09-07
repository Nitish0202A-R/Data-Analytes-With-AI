SELECT * FROM employee;


INSERT INTO employee(name,position,departmant,date_hring,salary)
       VALUES('Nitish kumar','Data Analyst','Data science','2022-05-16',65000.00),
	         ('Ravi Kumar','Laptop Rapring','Rpring','2022-05-11',45000.00),
			 ('Rohit KUmar','Data Analyst','Data science','2023-05-12',65000.00),
			 ('Abhi','Frontend deveploer','Developer ','2025-05-16',75000.00),
			 ('Pradhan Kumar','Data Analyst','Data science','2026-05-16',55000.00);




ALTER TABLE employee
RENAME COLUMN postiion TO position;


SELECT * FROM employee;


TRUNCATE TABLE employee;
TRUNCATE TABLE employee RESTART IDENTITY;
