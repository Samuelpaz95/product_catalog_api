USE catalog_db;
DROP TABLE IF EXISTS noti_to_users;
DROP TABLE IF EXISTS action_in_notifications;
DROP TABLE IF EXISTS updated_fields;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS user;

CREATE TABLE product (
    product_ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(30) NOT NULL UNIQUE,
    product_name VARCHAR(100) NOT NULL,
    product_price DOUBLE,
    brand VARCHAR (100)
);

CREATE TABLE user (
    user_ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR (100) NOT NULL,
    username VARCHAR (30) NOT NULL UNIQUE,
    password VARCHAR (100) NOT NULL,
    email VARCHAR (100) NOT NULL UNIQUE,
    user_level INT(1) NOT NULL
);

CREATE TABLE notifications (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    responsable_id INT(11) NOT NULL,
    action VARCHAR(50),
    CONSTRAINT fk_user_notification FOREIGN KEY (responsable_id) REFERENCES user(user_ID) ON DELETE CASCADE
);

CREATE TABLE noti_to_users (
    noti_id INT(11) NOT NULL,
    user_id INT(11) NOT NULL,
    CONSTRAINT fk_noti_to_user FOREIGN KEY (user_ID) REFERENCES user(user_ID) ON DELETE CASCADE,
    CONSTRAINT fk_noti_to_noti FOREIGN KEY (noti_id) REFERENCES notifications(id) ON DELETE CASCADE
);

CREATE TABLE updated_fields (
    field_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    field_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE action_in_notifications (
    noti_id INT(11) NOT NULL,
    field_id INT(11) NOT NULL,
    CONSTRAINT fk_action_notification FOREIGN KEY (noti_id) REFERENCES notifications(id) ON DELETE CASCADE,
    CONSTRAINT fk_action_field FOREIGN KEY (field_id) REFERENCES updated_fields(field_id) ON DELETE CASCADE
);
