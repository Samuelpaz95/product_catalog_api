from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:
    url = 'mysql://{user}:{password}@localhost/catalog_db'
    __Session = sessionmaker()
    __session = __Session()
    def __init__(self, user:str=None, password:str=None) -> None:
        if user is None or password is None:
            self.config_engine(user, password)
    
    def config_engine(self, user:str, password:str) -> None:
        self.__engine = create_engine(self.url.format(user=user, password=password))
        self.__Session.configure(bind=self.__engine)
        self.__session.close()
        self.__session = self.__Session()
    @property
    def session(self):
        return self.__session
    


Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    porduct_ID = Column(Integer, nullable=False, primary_key=True)
    sku = Column(String(30), nullable=False, unique=True)
    product_name = Column(String(100), nullable=False)
    product_price = Column(Float)
    brand = Column(String(100))
    def __init__(self, sku:str, name:str, price:float, brand:str) -> None:
        self.sku = sku
        self.product_name = name
        self.product_price = price
        self.brand = brand

class User:
    user_ID = Column(Integer, nullable=False, primary_key=True)
    full_name = Column(String(100), nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    user_level = Column(Integer, nullable=False)
    def __init__(self, full_name:str, username:str, password:str, email:str, is_admin:int=0):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
        self.user_level = is_admin