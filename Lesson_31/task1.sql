-- Task 1 - Joins

-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- - write a query in SQL to display the first name, last name, department number, and department name for each employee
-- - write a query in SQL to display the first and last name, department, city, and state province for each employee
-- - write a query in SQL to display the first name, last name, department number, and department name,
-- for all employees for departments 80 or 40
-- - write a query in SQL to display all departments including those where does not have any employee
-- - write a query in SQL to display the first name of all employees including the first name of their manager
-- - write a query in SQL to display the job title, full name (first and last name ) of the employee,
-- and the difference between the maximum salary for the job and the salary of the employee
-- - write a query in SQL to display the job title and the average salary of employees
-- - write a query in SQL to display the full name (first and last name), and salary of those employees
-- who work in any department located in London
-- - write a query in SQL to display the department name and the number of employees in each department

-- Query to display the first name, last name, department number, and department name for each employee
SELECT
  employees.first_name,
  employees.last_name,
  employees.department_id,
  departments.depart_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;

-- Query to display the first and last name, department, city, and state province for each employee
SELECT
  employees.first_name,
  employees.last_name,
  employees.department_id,
  departments.depart_name,
  locations.city,
  locations.state_province
FROM employees
LEFT JOIN departments USING(department_id)
LEFT JOIN locations USING(location_id);

-- Query to display the first name, last name, department number, and department name,
-- for all employees for departments 80 or 40
SELECT
  employees.first_name,
  employees.last_name,
  employees.department_id,
  departments.depart_name
FROM employees
LEFT JOIN departments USING(department_id)
WHERE employees.department_id = 40 OR employees.department_id = 80;

-- Query to display all departments including those where does not have any employee
SELECT * FROM departments

-- Query to display the first name of all employees including the first name of their manager
SELECT
  empl_1.first_name AS 'Employee first name',
  COALESCE(empl_2.first_name, NULL) AS 'Manager first name'
FROM employees AS empl_1
LEFT JOIN employees AS empl_2
ON empl_1.manager_id = empl_2.employee_id;

-- Query to display the job title, full name (first and last name ) of the employee,
-- and the difference between the maximum salary for the job and the salary of the employee
SELECT
  jobs.job_title,
  employees.first_name || ' ' || employees.last_name AS 'employee_full_name',
  (jobs.max_salary - employees.salary) AS dif_salary
FROM employees
LEFT JOIN jobs USING (job_id);

-- Query to display the job title and the average salary of employees
SELECT
  jobs.job_title,
  AVG(employees.salary) AS 'average salary'
FROM jobs
INNER JOIN employees USING (job_id)
GROUP BY jobs.job_title;

-- Query to display the full name (first and last name), and salary of those employees
-- who work in any department located in London
SELECT
  employees.first_name || ' ' || employees.last_name AS 'employee_full_name',
  locations.city AS 'department_city'
FROM employees
LEFT JOIN departments USING(department_id)
LEFT JOIN locations USING(location_id)
WHERE locations.city = 'London';

-- Query to display the department name and the number of employees in each department
SELECT
  employees.first_name || ' ' || employees.last_name AS 'employee_full_name',
  employees.salary,
  locations.city AS 'department_city'
FROM employees
LEFT JOIN departments USING(department_id)
LEFT JOIN locations USING(location_id)
WHERE locations.city = 'London';
