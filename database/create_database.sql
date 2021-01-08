CREATE DATABASE catalog_db;

CREATE USER 'catalog_admin'@'localhost' IDENTIFIED BY 'adminpassword';
CREATE USER 'anonymous_user'@'localhost' IDENTIFIED BY '';

GRANT SELECT, INSERT, UPDATE, DELETE ON catalog_db.* TO 'catalog_admin'@'localhost';
GRANT SELECT ON catalog_db.* TO 'anonymous_user'@'localhost';