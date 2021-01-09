from sqlalchemy import create_engine, or_
from sqlalchemy import Column, Integer, String, Float, MetaData
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

    def MetaData(self):
        return MetaData()
    


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
        return product_json

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

    def save(self, db:Database) -> dict:
        existing_users = db.session.query(User.username, User.email).filter(or_(User.username==self.username, User.email==self.email)).all()
        notify = self.create_notify(existing_users)
        if not existing_users:
            db.session.add(self)
            db.session.commit()
        return notify
    def create_notify(self, existing_users):
        notify = {
            'done': True,
            'message': 'Successfully registered user'
        }
        if existing_users:
            notify['done'] = False
            notify['message'] = 'This field/s is in use: '
            for fields in existing_users:
                if self.username in fields:
                    notify['message'] += 'username, '
                if self.email in fields:
                    notify['message'] += 'email, '
            notify['message'] = notify['message'][:-2]
        return notify

        


        