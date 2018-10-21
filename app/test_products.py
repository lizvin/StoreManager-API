import unittest
import json

from app.api.v1.views.products import Products
from app import app

class TestProducts(unittest.TestCase):
    def setUp(self):
        self.tests = app.test_client()
        self.tests.testing = True

        product_data = json.dumps({
        "name" : "Bia",
        "category" : "Electronics",
        "price" : 600
        })

        order_sale = json.dumps({
            "name" : "Bia",
            "category" : "Electronics",
            "price" : 600
        })

        self.create_product = self.tests.post('/products', data=product_data, content_type="application/json")
        self.create_sale = self.tests.post('/products', data=order_sale, content_type="application/json")
    
    def tearDown(self):
        self.tests = None

    def test_get_products(self):
        result = self.tests.get("/products", content_type="application/json")
        self.assertEqual(result.status_code, 200)

    def test_post_products(self):
        order_data = json.dumps({
            "name" : "Bia",
            "category" : "Electronics",
            "price" : 500
        })

        res = self.tests.post('/products', data=order_data, content_type="application/json")
        self.assertEqual(res.status_code, 200)
   

    

    # def test_get(self):
    #     result = self.tests.get("/products")
    #     data = json.loads(result.get_data().decode('UTF-8'))
    #     self.assertEqual(data, {'message': "Products successfully fetched", "products":[]})

    # # def test_get_invalid_dataset(self):
    # #     dataset = {"name":"Pizza", "category":"Electronic", "price":"900"}
    # #     result = self.tests.post("/products", data=json.dumps(dataset))
    # #     data = json.loads(result.get_data().decode('UTF-8'))
    # #     self.assertEqual(result.status_code, 406)
    # #     self.assertEqual(data, {'message': "Invalid data payload"})