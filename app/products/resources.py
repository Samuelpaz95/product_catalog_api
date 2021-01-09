from ..common import CommonListResource, CommonResource
from ..models import Product

class ProductListResource(CommonListResource):
    class_model = Product


class ProductResource(CommonResource):
    class_model = Product
