from flask import Blueprint
from flask import session, request
from flask_restful import Resource
from flask_login import login_required
from werkzeug.security import generate_password_hash

from .error_handling import ObjectNotFound
from ..db_conncetion import db
from ..models import Base, User
from ..notifications.models import NotificateAction, Notifications, NotifyToUser, UpdatedFields

resource_bp = Blueprint('resource_bp', __name__)

class CommonListResource(Resource):
    """
    This is a resource to obtain a listing of a generic table model of a database
    """
    class_model: Base = None

    def get(self) -> dict:
        elements = db.get_all(self.class_model)
        results = []
        for user in elements:
            results.append(user.to_json())
        return results

    @login_required
    def post(self) -> dict:
        data = request.get_json()
        data = self._encrypt_passwords(data)
        new_element = self.class_model(**data)
        db.save(new_element)
        return {'done': True, 'msg': f'{new_element.__tablename__} added successfully'}, 201

    def _encrypt_passwords(self, data):
        if 'password' in data:
            data['password'] = generate_password_hash(data['password'])
        return data

class CommonResource(CommonListResource):
    """
    This is a resource to manage a specific element of a database, among the actions is get, update, delete
    """
    class_model: Base = None

    def get(self, element_ID: int) -> dict:
        element = db.get_by_id(self.class_model, element_ID)
        if element is None:
            raise ObjectNotFound(
                f'This {self.class_model.__tablename__} does not exist')
        return element.to_json()

    @login_required
    def put(self, element_ID: int) -> dict:
        element = db.get_by_id(self.class_model, element_ID)
        if element is None:
            raise ObjectNotFound('This element does not exist')
        data = request.get_json()
        data = self._encrypt_passwords(data)
        input_fields = set(data.keys())
        fields = set(element.attributes())
        incorrect_fields = input_fields - fields
        response = {'done':False}
        if not incorrect_fields:
            updated_fields = fields & input_fields
            db.update(self.class_model, element_ID, data)
            notify = self.__create_notifiation(updated_fields)
            self.__notify_to_users(notify)
            response['done'] = True
            response['msg'] = f'{element.__tablename__} update successfully'
            response['update_fields'] = list(updated_fields)
        else:
            response['incorrect_fields'] = list(incorrect_fields)
        return response

    @login_required
    def delete(self, element_ID: int) -> dict:
        element = db.get_by_id(self.class_model, element_ID)
        if element is None:
            raise ObjectNotFound('This element does not exist')
        db.delete(element)
        return {'done': True, 'deleted_element_data': element.to_json()}

    def __create_notifiation(self, updated_fields:set) -> Notifications:
        """
        Create a notification of the update made by the current user

        Arguments:
            updated_fields (set): Is the set of fields that will be updated

        Returns:
            `Notifications` -- A new notification about the updated fields.
        """
        notify = Notifications(int(session['_user_id']), 'update')
        db.save(notify)
        registered_fields = db.get_all(UpdatedFields)
        for index, updated_field in enumerate(updated_fields):
            new_field = UpdatedFields(updated_field)
            if new_field in registered_fields:
                new_field: UpdatedFields = registered_fields[index]
            else:
                db.save(new_field)
            db.save(NotificateAction(notify.id, new_field.field_id))
        return notify

    def __notify_to_users(self, notify:Notifications):
        """notifies other administrators about changes

        Arguments:
            notify (Notifications): The notification.
        """
        users = db.get_all(User)
        for user in users:
            if not user.user_ID == int(session['_user_id']):
                db.save(NotifyToUser(notify.id, user.user_ID))
