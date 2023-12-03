-- Task 1 - Create a table
-- Create a table of your choice, rename it, and add a new column.
-- Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.
-- NOTE: Implemented by PostgreSQL

Database: lesson30

DROP DATABASE IF EXISTS lesson30;

CREATE DATABASE lesson30
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

DROP TABLE IF EXISTS new_dantabase;
DROP TABLE IF EXISTS Avengers;

CREATE TABLE IF NOT EXISTS new_dantabase (
    id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	real_name TEXT NOT NULL
);

INSERT INTO new_dantabase (name, real_name) VALUES 
	('Iron Man', 'Tony Stark'),
	('Captain America', 'Steve Rogers'),	
	('Hulk', 'Bruce Banner');
	
ALTER TABLE new_dantabase RENAME TO Avengers;
ALTER TABLE Avengers ADD COLUMN actor text;	

UPDATE Avengers SET actor = 'Robert Downey Jr.' WHERE name = 'Iron Man';
UPDATE Avengers SET actor = 'Chris Evans' WHERE name = 'Captain America';
UPDATE Avengers SET actor = 'Mark Ruffalo' WHERE name = 'Hulk';


INSERT INTO Avengers (name, real_name, actor) VALUES 
	('Thor', '	Thor Odinson', 'Chris Hemsworth'),
	('Black Widow', 'Natasha Romanoff', 'Scarlett Johansson'),	
	('Quicksilver', 'Pietro Maximoff', 'Aaron Taylor-Johnson'),
	('Falcon', 'Samuel Wilson', 'Anthony Mackie'),
	('Hawkeye', 'Clint Barton', 'Jeremy Renner'),
	('Vision', 'Vision', 'Paul Bettany'),
	('Scarlet Witch', 'Wanda Maximoff', 'Elizabeth Olsen');

DELETE FROM Avengers WHERE real_name = 'Pietro Maximoff';
SELECT * FROM Avengers
