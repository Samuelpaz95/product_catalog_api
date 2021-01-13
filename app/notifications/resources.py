from flask_login.utils import login_required
from flask_restful import Resource
from flask import session

from app.common.error_handling import ObjectNotFound
from ..db_conncetion import db

class NotificationListResource(Resource):
    @login_required
    def get(self) -> dict:
        result = db.call_procedure('GetNotifications', user_ID=int(session['_user_id']))
        notification_list = []
        json_row = {'id': -1, 'field_name': []}
        for row in result['data']:
            if not row[0] == json_row['id']:
                json_row = {'id': row[0], 'field_name': []}
            json_row = self.__fill_notifications_list(row, json_row, result['keys'])
            if not json_row in notification_list:
                notification_list.append(json_row)
        return notification_list
    
    def __fill_notifications_list(self, row:list, json_row:dict, field_names:list):
        for field, value in zip(field_names, row):
            if not field == 'field_name':
                json_row[field] = value
            else:
                json_row[field].append(value)
        return json_row

class NotificationResource(NotificationListResource):
    def get(self, noti_id) -> dict:
        notifications_list = super().get()
        (result, found, index) = ({}, False, -1)
        while not found:
            index += 1
            found = notifications_list[index]['id'] == noti_id
        if found:
            result = notifications_list[index]
        else:
            raise ObjectNotFound(
                f'This notification does not exist')
        return result