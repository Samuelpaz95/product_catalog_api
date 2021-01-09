from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
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

class User(Base):
    __tablename__ = 'user'
    user_ID = Column(Integer, nullable=False, primary_key=True)
    full_name = Column(String(100), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    user_level = Column(Integer, nullable=False)
    def __init__(self, full_name:str, username:str, password:str, email:str, user_level:int=0):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
        self.user_level = user_level
    def to_json(self) -> dict:
        result = {
            'user_ID': self.user_ID,
            'full_name': self.full_name,
            'password': self.password,
            'email': self.email
        }
        return result
    def attributes(self) -> list:
        return list(self.__dict__.keys())[1:]
    def __repr__(self)-> str:
        return f'User{self.username}'
    def __str__(self) -> str:
        return f'{self.full_name}'