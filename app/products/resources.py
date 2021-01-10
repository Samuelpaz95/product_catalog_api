from multiprocessing import Value
from ..common import CommonListResource, CommonResource
from ..models import Product

class ProductListResource(CommonListResource):
    class_model = Product


class ProductResource(CommonResource):
    class_model = Product
    counter = {}
    def get(self, element_ID: int) -> dict:
        out = self.count_product_views(element_ID)
        results = super().get(element_ID=element_ID)
        results['views'] = out
        return results

    def count_product_views(self, product_ID):
        if product_ID not in self.counter:
            self.counter[product_ID] = Value('i', 0)
        with self.counter[product_ID].get_lock():
            self.counter[product_ID].value += 1
            out = self.counter[product_ID].value
        return out