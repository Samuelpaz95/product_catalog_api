from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    id_name = 'product_ID'
    product_ID = Column(Integer, nullable=False, primary_key=True)
    sku = Column(String(30), nullable=False, unique=True)
    product_name = Column(String(100), nullable=False)
    product_price = Column(Float)
    brand = Column(String(100))
    def __init__(self, sku:str, product_name:str, product_price:float, brand:str) -> None:
        self.sku = sku
        self.product_name = product_name
        self.product_price = product_price
        self.brand = brand
    def to_json(self) -> dict:
        product_json = self.__dict__.copy()
        product_json.pop(list(product_json.keys())[0])
        product_json['product_ID'] = self.product_ID
        return product_json
    def attributes(self) -> list:
        return list(self.__dict__.keys())[1:]
    def __repr__(self)-> str:
        return f'User{self.sku}_{self.brand}'
    def __str__(self) -> str:
        return f'{self.product_name}'

class User(Base, UserMixin):
    __tablename__ = 'user'
    id_name = 'user_ID'
    user_ID = Column(Integer, nullable=False, primary_key=True)
    full_name = Column(String(100), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    user_level = Column(Integer, nullable=False)
    def __init__(self, full_name:str, username:str, password:str, email:str, user_level:int=0):
        self.full_name = full_name
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.user_level = user_level
    
    def verify_password(self, password:str) -> bool:
        return check_password_hash(self.password, password)

    def to_json(self) -> dict:
        result = {
            'user_ID': self.user_ID,
            'full_name': self.full_name,
            'username': self.username,
            'email': self.email
        }
        return result

    def attributes(self) -> list:
        attributes = list(self.__dict__.keys())[1:]
        attributes.remove('password')
        attributes.append('password')
        return attributes

    def get_id(self):
        return str(self.user_ID)

    def __repr__(self)-> str:
        return f'User{self.username}'
    def __str__(self) -> str:
        return f'{self.full_name}'