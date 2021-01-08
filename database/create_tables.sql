USE catalog_db;

DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS user;

CREATE TABLE product (
    porduct_ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(30) NOT NULL UNIQUE,
    product_name VARCHAR(100) NOT NULL,
    product_price DOUBLE,
    brand VARCHAR (100)
);

CREATE TABLE user (
    user_ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR (100) NOT NULL,
    username VARCHAR (30) NOT NULL UNIQUE,
    password VARCHAR (30) NOT NULL,
    email VARCHAR (100) NOT NULL UNIQUE,
    user_level INT(1) NOT NULL,
)