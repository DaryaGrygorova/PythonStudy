-- Task 2 - Select queries
-- Use the sample SQLite database hr.db (from LMS)
--
-- As a solution to HW, create a file named 'task2.sql' with all SQL queries:
--
--  - write a query to display the names (first_name, last_name) using alias name
-- "First Name", "Last Name" from the table of employees;
--  - write a query to get the unique department ID from the employee table
--  - write a query to get all employee details from the employee table ordered by first name,
--  descending
--  - write a query to get the names (first_name, last_name), salary, PF of all the employees
-- (PF is calculated as 12% of salary)
--  - write a query to get the maximum and minimum salary from the employees table
--  - write a query to get a monthly salary (round 2 decimal places) of each and every employee

-- Query to display the names (first_name, last_name) using alias name
-- "First Name", "Last Name" from the table of employees;
SELECT first_name AS 'First name', last_name AS 'Last name' FROM employees;

-- Query to get the unique department ID from the employee table
SELECT DISTINCT department_id FROM employees;

-- Query to get all employee details from the employee table ordered by first name, descending
SELECT * FROM employees ORDER BY last_name DESC, first_name DESC;

-- Query to get the names (first_name, last_name), salary, PF of all the employees
-- (PF is calculated as 12% of salary)
SELECT first_name, last_name, salary, salary * 0.12 AS PF FROM employees;

-- Query to get the maximum and minimum salary from the employees table
SELECT MAX(salary) AS 'Salary (max)', MIN(salary) AS 'Salary (min)' FROM employees;

-- Query to get a monthly salary (round 2 decimal places) of each and every employee
SELECT first_name, last_name, ROUND(salary, 2) AS 'monthly_salary' FROM employees;
