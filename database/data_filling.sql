USE catalog_db;
INSERT INTO product (sku, product_name, product_price, brand)
VALUES ('SPORT-XYZ-BLN-41', 'sports shoe', 99.99, 'Nike'),
       ('TOOLS-AVE-PEW-00', 'carpentry hammer', 24.99, 'Tramontina'),
       ('TOYSS-SKY-EWF-23', 'toy fire truck', 54.41, 'Hasbro'),
       ('TOYSS-SEA-DER-43', 'rubber duck', 2.65, 'Hasbro'),
       ('ELECT-ITE-UWU-12', 'Notebook', 812.00, 'HP Notebooks');

INSERT INTO user (full_name, username, password, email, user_level)
VALUES ('El Administrador', 'admin', 'pbkdf2:sha256:150000$KI8UCkD0$383222dbb7d388968cf749fa37d62d64ed33177beb91ff829d8fb8cee32937f9', "fake_email@gmail.com", 0),
       ('the Admin', 'other_admin', 'pbkdf2:sha256:150000$tSLbrKO0$0cf954584feb8c5143c9cda9a60d787a2c762a45004e846646a4ae9a328d852c', "other_fake_email@gmail.com", 0)
       