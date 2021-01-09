from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

class Database:
    uri = 'mysql://{user}:{password}@localhost/catalog_db'
    __Session = sessionmaker()
    __session:__Session = __Session()
    def __init__(self, user:str=None, password:str=None) -> None:
        if user is None or password is None:
            self.config_engine(user, password)

    def config_engine(self, user:str, password:str) -> None:
        self.__engine = create_engine(self.uri.format(user=user, password=password))
        self.__Session.configure(bind=self.__engine)
        self.__session.close()
        self.__session = self.__Session()

    def save(self, element:Base) -> None:
        self.session.add(element)
        self.session.commit()

    def update(self, cls:Base, id_field:int, data:dict) -> int:
        product = db.session.query(cls).filter_by(**{f"{cls.__tablename__}_ID":id_field})
        rows_affected = product.update(data)
        db.session.commit()
        return rows_affected

    def delete(self, element:Base) -> None:
        self.session.delete(element)
        self.session.commit()

    def get_all(self, cls:Base) -> None:
        return self.session.query(cls).all()

    def get_by_id(self, cls:Base, id:int) -> Base:
        return self.session.query(cls).get(id)

db = Database()