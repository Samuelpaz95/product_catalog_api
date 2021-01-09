## Catalog API

Open this url in web browser 
```localhost:5000/```

### Available resources
- ```/products``` GET request, get a json with registered products.

output:
```json
{
    "1": {
        "brand": "Nike",
        "product_ID": 1,
        "product_name": "sports shoe",
        "product_price": 99.99,
        "sku": "SPORT-XYZ-BLN-41"
    },
    "2": {
        "brand": "Tramontina",
        "product_ID": 2,
        "product_name": "carpentry hammer",
        "product_price": 24.99,
        "sku": "TOOLS-AVE-PEW-00"
    },
    "3": {
        "brand": "Hasbro",
        "product_ID": 3,
        "product_name": "toy fire truck",
        "product_price": 54.41,
        "sku": "TOYSS-SKY-EWF-23"
    },
    ...
}
```
- ```/users``` GET request, get a json with registered users.
```json
{
    "1": {
        "email": "fake_email@gmail.com",
        "full_name": "El Administrador",
        "username": "admin"
    },
    "2": {
        "email": "other_fake_email@gmail.com",
        "full_name": "the Admin",
        "username": "other_admin"
    }
}
```
- ```/add_user``` POST request, Add a user to the database, get a confirm json.

input example:
```json
{
    "full_name" : "Francis Mamani",
    "username" : "frans123",
    "password" : "apassword",
    "email" : "fransmani@gmail.com"
}
```
output:
```json
{
    "done": true,
    "message": "Successfully registered user"
}
```
- ```/users/update/<user_ID>``` PUT request, update user fields.

input example:
```json
{
    "username" : "fulano1234"
}
```
output:
```json
{
    "done": true,
    "message": "action completed successfully",
    "updated_fields": [
        "username"
    ],
    "user_ID": "1"
}
```
output error:
```json
{
    "done": false,
    "message": "Invalid fields"
}
```
- ```/users/delete/<user_ID>``` DELETE request, delete a user.

example *"/users/delete/1"*
output:
```json
{
    "deleted_user_data": {
        "email": "fake_email@gmail.com",
        "full_name": "El Administrador",
        "username": "fulano1234"
    },
    "done": true
}
```
- ```/products/<product_ID>``` GET request, get a json with the data of a product.

example *"/products/1"*

output:
```json
{
    "brand": "Nike",
    "product_ID": 1,
    "product_name": "sports shoe",
    "product_price": 99.99,
    "sku": "SPORT-XYZ-BLN-41",
    "views": 1
}
```
- ```/products/update/<product_ID>``` PUT request, update product fields.
input example:
```json
{
    "product_price" : 200
}
```
output:
```json
{
    "done": true,
    "message": "action completed successfully",
    "product_ID": "1",
    "updated_fields": [
        "product_price"
    ]
}
```
error:
```json
{
    "done": false,
    "message": "Invalid fields"
}
```
- ```/products/delete/<product_ID>``` DELETE request, delete a product.

example *"/products/delete/5"*:
output:
```json
{
    "done": true,
    "element_deleted": {
        "brand": "HP Notebooks",
        "product_ID": 5,
        "product_name": "Notebook",
        "product_price": 812.0,
        "sku": "ELECT-ITE-UWU-12"
    },
    "message": "Product removed successfully"
}
```