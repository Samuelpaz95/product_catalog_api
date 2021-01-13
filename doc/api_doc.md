## Catalog API

Open this url in web browser 
```localhost:5000/```

### Available resources
- ```api/products/``` GET request, get a json with registered products.

    - output example:
        ```json
        [
            {
                "sku": "SPORT-XYZ-BLN-41",
                "brand": "Nike",
                "product_name": "sports shoe",
                "product_ID": 1,
                "product_price": 99.99
            },
            {
                "sku": "TOOLS-AVE-PEW-00",
                "brand": "Tramontina",
                "product_name": "carpentry hammer",
                "product_ID": 2,
                "product_price": 24.99
            },
            {
                "sku": "TOYSS-SKY-EWF-23",
                "brand": "Hasbro",
                "product_name": "toy fire truck",
                "product_ID": 3,
                "product_price": 54.41
            },
            {
                "sku": "TOYSS-SEA-DER-43",
                "brand": "Hasbro",
                "product_name": "rubber duck",
                "product_ID": 4,
                "product_price": 2.65
            },
            {
                "sku": "ELECT-ITE-UWU-12",
                "brand": "HP Notebooks",
                "product_name": "Notebook",
                "product_ID": 5,
                "product_price": 812.0
            }
        ]
        ```
- ```api/products/<id>``` GET request, get a json with registered products.

    - output example
        ```json
        // with [url]:[port]/api/products/1
        {
            "sku": "SPORT-XYZ-BLN-41",
            "brand": "Nike",
            "product_name": "sports shoe",
            "product_ID": 1,
            "product_price": 99.99,
            "views": 1
        }
        ```
For the following resources it requires an administrator session.
- ```/login``` POST request, start a session that expires in 10 min.

    - input example:
        ```json
        {
            "username": "admin",
            "password": "password"
        }
        ```
    - output example:

        ```json
        {
            "email": "fake_email@gmail.com",
            "full_name": "El Administrador",
            "user_ID": 1
        }
        ```
- ```/logout``` GET request, it close the session.

- ```api/products/``` POST request, get a json with registered users.

    - input example:
        ```json
        {
            "sku" : "ASDGE-ASDF-AWE-21",
            "product_name" : "cup",
            "product_price" : 9.99,
            "brand" : "crystaline"
        }
        ```
        output example:
        ```json
        {
            "done": true,
            "msg": "product added successfully"
        }
        ```
- ```api/products/<id>``` PUT request, it update the product data.

    - input example:
        ```json
        // with [url]:[port]/api/products/6
        {
            "product_price" : 8.41
        }
        ```
    - output example:
        ```json
        {
            "done": true,
            "msg": "product update successfully",
            "update_fields": [
                "product_price"
            ]
        }
        ```
- ```api/products/<id>``` DELETE request, it delete the product data.

    - output exaple:
        ```json
        // with [url]:[port]/api/products/6
        {
            "done": true,
            "deleted_element_data": {
                "sku": "ASDGE-ASDF-AWE-21",
                "brand": "crystaline",
                "product_name": "cup",
                "product_ID": 6,
                "product_price": 9.41
            }
        }
        ```
- ```api/users/``` GET request, get a json with registered users.

    - output example:
        ```json
        [
            {
                "user_ID": 1,
                "full_name": "El Administrador",
                "username": "admin",
                "email": "fake_email@gmail.com"
            },
            {
                "user_ID": 2,
                "full_name": "the Admin",
                "username": "other_admin",
                "email": "other_fake_email@gmail.com"
            }
        ]
        ```
- ```api/users/``` POST request, Add a user to the database, get a confirm json.

    - input example:
        ```json
        {
            "full_name" : "Francis Mamani",
            "username" : "frans123",
            "password" : "apassword",
            "email" : "fransmani@gmail.com"
        }
        ```
    - output example:
        ```json
        {
            "done": true,
            "msg": "user added successfully"
        }
        ```
- ```api/users/<user_ID>``` GET request, get a user data.
    - output example
        ```json
        // with [url]:[port]/api/users/3 
        {
            "user_ID": 3,
            "full_name": "Francis Mamani",
            "username": "frans123",
            "email": "fransmani@gmail.com"
        }
        ```
- ```api/users/<user_ID>``` PUT request, it update the user data.
    - input example:
        ```json
        {
            "username" : "frans6432",
            "password" : "mynewpassword"
        }
        ```
    - output example:
        ```json
        {
            "done": true,
            "msg": "user update successfully",
            "update_fields": [
                "username",
                "password"
            ]
        }
        ```
    - output error example:
        ```json
        {
            "done": false,
            "incorrect_fields": [
                "usernsame",
                "passwodrd"
            ]
        }
        ```
- ```api/users/<user_ID>``` DELETE request, it delete the user data.
    - output example:
        ```json
        {
            "done": true,
            "deleted_element_data": {
                "user_ID": 3,
                "full_name": "Francis Mamani",
                "username": "frans6432",
                "email": "fransmani@gmail.com"
            }
        }
        ```
    Login with other user for example, user ```/ligin``` username: "other_user", password: "password2"
- ```notifications/``` GET request, get notifications of updates for current user.
    - output example:
        ```json
        [
            {
                "id": 1,
                "field_name": [
                    "product_price"
                ],
                "user_ID": 2,
                "responsable_id": 1,
                "responsable_full_name": "El Administrador",
                "responsable_email": "fake_email@gmail.com",
                "action": "update"
            },
            {
                "id": 2,
                "field_name": [
                    "username",
                    "password"
                ],
                "user_ID": 2,
                "responsable_id": 1,
                "responsable_full_name": "El Administrador",
                "responsable_email": "fake_email@gmail.com",
                "action": "update"
            }
        ]
        ```