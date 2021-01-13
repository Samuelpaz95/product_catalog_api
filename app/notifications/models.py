from sqlalchemy import Column, Integer, String, ForeignKey
from ..models import Base

class UpdatedFields(Base):
    __tablename__ = 'updated_fields'
    field_id = Column(Integer, nullable=False, primary_key=True)
    field_name = Column(Integer, nullable=False, unique=True)

    def __init__(self, field_name:str) -> None:
        self.field_name = field_name

    def __eq__(self, other) -> bool:
        return self.field_name == other.field_name

class Notifications(Base):
    __tablename__ = 'notifications'
    id_name = 'id'
    id = Column(Integer, nullable=False, primary_key=True)
    responsable_id = Column(Integer, ForeignKey('user.user_ID'), nullable=False)
    action = Column(String(50))

    def __init__(self, responsable_id:int, action:str) -> None:
        self.responsable_id = responsable_id
        self.action = action

class NotificateAction(Base):
    __tablename__ = 'action_in_notifications'
    noti_id = Column(Integer, ForeignKey('notifications.id'), nullable=False, primary_key=True)
    field_id = Column(Integer, ForeignKey('updated_fields.field_id'), nullable=False, primary_key=True)
    def __init__(self, noti_id:int, field_id:int) -> None:
        self.noti_id = noti_id
        self.field_id = field_id

class NotifyToUser(Base):
    __tablename__ = 'noti_to_users'
    noti_id = Column(Integer, ForeignKey('notifications.id'), nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_ID'), nullable=False, primary_key=True)
    def __init__(self, noti_id:int, user_id:int) -> None:
        self.noti_id = noti_id
        self.user_id = user_id
        