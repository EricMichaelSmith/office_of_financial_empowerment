CREATE DATABASE IF NOT EXISTS ofe;
USE ofe;
DROP TABLE IF EXISTS clients;
CREATE TABLE clients
	(
	last_name varchar(20) DEFAULT NULL,
	first_name varchar(20) DEFAULT NULL,
	birthdate date DEFAULT NULL,
	ssn char(9) DEFAULT NULL,
	language_spoken int(2) unsigned DEFAULT NULL, # 00 = English, 01 = Spanish, 02 = Chinese, 03 = Russian, 04 = Haitian-Creole, 05 = Korean, etc.
	email varchar(30) DEFAULT NULL,
	phone1 char(10) DEFAULT NULL,
	phone2 char(10) DEFAULT NULL,
	banking boolean DEFAULT NULL, # TRUE if on the banking action plan
	credit boolean DEFAULT NULL,
	debt boolean DEFAULT NULL,
	savings boolean DEFAULT NULL,
	does_not_make_living_wage boolean DEFAULT NULL,
	receives_government_benefits boolean DEFAULT NULL,
	PRIMARY KEY (ssn));

INSERT INTO clients (last_name, first_name, birthdate, ssn, language_spoken, email, phone1, phone2, banking, credit, debt, savings, does_not_make_living_wage, receives_government_benefits)
VALUES ('Haynes', 'Candida', '1993-01-01', '123456789', 00, 'candida@foo.com', '2789662910', NULL, 0, 0, 0, 1, 0, 1),
	   ('Bell', 'William', '1965-04-27', '987654321', 00, 'williambe@yahoo.com', '2394770579', '2876883778', 0, 1, 1, 0, 0, 0),
	   ('Smith', 'Eric', '1988-08-09', '271828182', 00, NULL, '9802374589', NULL, 1, 0, 1, 1, 1, 1);