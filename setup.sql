-- create the databases
CREATE DATABASE IF NOT EXISTS tdb;

-- create the users for each database
CREATE USER 'tdbuser'@'localhost' IDENTIFIED BY 'password';
GRANT CREATE, ALTER, INDEX, LOCK TABLES, REFERENCES, UPDATE, DELETE, DROP, SELECT, INSERT ON tdb.* TO 'tdbuser'@'localhost';

FLUSH PRIVILEGES;