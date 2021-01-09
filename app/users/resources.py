from ..common import CommonListResource, CommonResource
from ..models import User

class UserListResource(CommonListResource):
    class_model = User

class UserResource(CommonResource):
    class_model = User
