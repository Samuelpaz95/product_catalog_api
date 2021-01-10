from flask.app import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

class Database:
    uri = 'mysql://{user}:{password}@localhost/catalog_db'
    __Session = sessionmaker()
    __session:__Session = __Session()
    def __init__(self, app:Flask=None) -> None:
        self.app = app
        if app is not None:
            self.config_engine(app.config['DATABASE_USER'], '')
    
    def init_app(self, app:Flask):
        self.app = app
        self.config_engine(app.config['DATABASE_USER'], '')

    def switch_to_admin(self):
        self.config_engine(self.app.config['DATABASE_ADMIN_USER'], self.app.config['DATABASE_ADMIN_PASSWORD'])
    
    def switch_to_anonymous(self):
        self.init_app(self.app)

    def config_engine(self, user:str, password:str) -> None:
        self.__engine = create_engine(self.uri.format(user=user, password=password))
        self.__Session.configure(bind=self.__engine)
        self.__session.close()
        self.__session = self.__Session()

    def save(self, element:Base) -> None:
        try:
            self.__session.add(element)
            self.__session.commit()
        except Exception as error:
            self.__session.rollback()
            raise error

    def update(self, cls:Base, id_field:int, data:dict) -> int:
        rows_affected = 0
        try:
            product = self.__session.query(cls).filter_by(**{f"{cls.__tablename__}_ID":id_field})
            rows_affected = product.update(data)
            self.__session.commit()
        except Exception as error:
            self.__session.rollback()
            raise error
        return rows_affected

    def delete(self, element:Base) -> None:
        try:
            self.__session.delete(element)
            self.__session.commit()
        except Exception as error:
            self.__session.rollback()
            raise error

    def get_all(self, cls:Base) -> None:
        return self.__session.query(cls).all()

    def get_by_id(self, cls:Base, id:int) -> Base:
        return self.__session.query(cls).get(id)

    def get_by(self, cls:Base, **kwargs:dict):
        return self.__session.query(cls).filter_by(**kwargs).all()

db = Database()