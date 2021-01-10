from flask_login.utils import login_required
from flask_restful import Resource

from ..models import User
from ..db_conncetion import db

class NotificationListResource(Resource):
    def get(self) -> dict:
        return {}

class NotificationResource(Resource):
    def delete(self, element_ID) -> dict:
        return super().get(element_ID)