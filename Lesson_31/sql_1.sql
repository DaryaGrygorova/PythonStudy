-- Database: Lesson_31

-- DROP DATABASE IF EXISTS "Lesson_31";

-- CREATE DATABASE "Lesson_31"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS groups_to_teachers;
DROP TABLE IF EXISTS groups_;
DROP TABLE IF EXISTS teachers;


CREATE TABLE IF NOT EXISTS students (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(200) NOT NULL,
	second_name VARCHAR(200) NOT NULL,
	age INTEGER NOT NULL,
	group_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS groups_ (
	id SERIAL PRIMARY KEY,
	group_name VARCHAR(200) NOT NULL,
	faculty VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS teachers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(200) NOT NULL,
	second_name VARCHAR(200) NOT NULL,
	age INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS groups_to_teachers (
	group_id INTEGER NOT NULL,
	teacher_id INTEGER NOT NULL,
	CONSTRAINT teacher_id_fk FOREIGN KEY (teacher_id) REFERENCES teachers (id),
	CONSTRAINT group_id_fk FOREIGN KEY (group_id) REFERENCES groups_ (id)
);

ALTER TABLE students
	ADD CONSTRAINT groups_students_fk 
	FOREIGN KEY (group_id) 
	REFERENCES groups_ (id);
	
INSERT INTO groups_
	(group_name, faculty) VALUES
		('TZ-71', 'Marketing'),
		('VL-83', 'Finance'),
		('BD-18', 'Psychology'),
		('CH-52', 'Chemistry');
	
INSERT INTO students 
	(first_name, second_name, age, group_id) 
	VALUES 
	('Ivan', 'Sirko', 21, 1),
	('Petro', 'Mohila', 22, 1),
	('Jessie', 'Pinkman', 24, 1);
	
INSERT INTO teachers 
	(first_name, second_name,age) 
	VALUES 
		('Walter', 'White', 50),
		('Jim', 'Clark', 45),
		('Mariia', 'Ivanova', 44);
	
INSERT INTO groups_to_teachers 
	(group_id, teacher_id) 
	VALUES 
		(4, 1),
		(1, 3),
		(2, 2);
	
-- SELECT * FROM groups_;
-- SELECT * FROM groups_ as gr JOIN groups_to_teachers as gr_tt ON gr.id = gr_tt.group_id;
-- SELECT * FROM groups_ JOIN groups_to_teachers ON groups_.id = groups_to_teachers.group_id;
-- SELECT * FROM groups_ FULL JOIN groups_to_teachers ON groups_.id = groups_to_teachers.group_id;
-- SELECT * FROM groups_ INNER JOIN groups_to_teachers ON groups_.id = groups_to_teachers.group_id;
-- SELECT * FROM groups_ LEFT JOIN groups_to_teachers ON groups_.id = groups_to_teachers.group_id;
-- SELECT * FROM groups_ RIGHT JOIN groups_to_teachers ON groups_.id = groups_to_teachers.group_id;

SELECT * FROM groups_ ORDER BY group_name;

-- SELECT * FROM students;
