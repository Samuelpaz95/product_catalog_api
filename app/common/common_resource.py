from flask import request, Blueprint
from flask_restful import Api, Resource
from .error_handling import ObjectNotFound
from ..db_conncetion import db
from ..models import Base

resource_bp = Blueprint('resource_bp', __name__)


class CommonListResource(Resource):
    class_model:Base = None
    def get(self) -> dict:
        elements = db.get_all(self.class_model)
        results = []
        for user in elements:
            results.append(user.to_json())
        return results

    def post(self) -> dict:
        db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
        data = request.get_json()
        new_element = self.class_model(**data)
        db.save(new_element)
        return {'done':True, 'msg': f'{new_element.__tablename__} added successfully'}, 201

class CommonResource(Resource):
    class_model:Base = None
    def get(self, element_ID:int) -> dict:
        element = db.get_by_id(self.class_model, element_ID)
        if element is None:
            raise ObjectNotFound(f'This {self.class_model.__tablename__} does not exist')
        return element.to_json()

    def put(self, element_ID:int) -> dict:
        db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
        element = db.get_by_id(self.class_model, element_ID)
        if element is None:
            raise ObjectNotFound('This element does not exist')
        data = request.get_json()
        input_fields = set(data.keys())
        fields = set(element.attributes())
        incorrect_fields = input_fields - fields
        if not incorrect_fields:
            db.update(self.class_model, element_ID, data)
            return {'done':True, 'msg': f'{element.__tablename__} update successfully','update_fields':list(fields & input_fields)}
        else:
            return {'done':False, 'incorrect_fields':list(incorrect_fields)}

    def delete(self, element_ID:int) -> dict:
        db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
        element = db.get_by_id(self.class_model, element_ID)
        if element is None:
            raise ObjectNotFound('This element does not exist')
        db.delete(element)
        return {'done':True, 'deleted_element_data':element.to_json()}