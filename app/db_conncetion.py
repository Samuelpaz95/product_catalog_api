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
        self.config_engine(app.config['DATABASE_USER'], app.config['DATABASE_PASSWORD'])

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
            product = self.__session.query(cls).filter_by(**{cls.id_name:id_field})
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
    
    def call_procedure(self, procedure_name:str, **kparameters) -> dict:
        """Call a stored procedure that returns nothing

        Arguments:

            procedure_name (str): The stored procedure name.
            kparameters (dict): (optional) The procedure parameters parameters.

        Returns:

            A `dict`:
                --`keys`: A `list` of the fields of a table.
                --`data`: the rows of the table.

        """
        if kparameters:
            parameters = ''.join(list(map(lambda arg: ", :"+arg, list(kparameters.keys()))))[2:]
            query = self.__session.execute(f'CALL {procedure_name}({parameters})', kparameters)
        else: 
            query = self.__session.execute(f'CALL {procedure_name}()')
        return {
            "keys": query.keys(),
            "data": query.fetchall()
        }

db = Database()