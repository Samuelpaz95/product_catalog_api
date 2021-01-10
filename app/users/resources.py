from flask_login.utils import login_required
from ..common import CommonListResource, CommonResource
from ..models import User

class UserListResource(CommonListResource):
    class_model = User
    @login_required
    def get(self) -> dict:
        return super().get()

class UserResource(CommonResource):
    class_model = User
    @login_required
    def get(self, element_ID) -> dict:
        return super().get(element_ID)
