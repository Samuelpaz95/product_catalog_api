CREATE DATABASE catalog_db;

CREATE USER 'catalog_admin'@'localhost' IDENTIFIED BY 'adminpassword';
GRANT SELECT, INSERT, UPDATE, DELETE ON catalog_db.* TO 'catalog_admin'@'localhost';