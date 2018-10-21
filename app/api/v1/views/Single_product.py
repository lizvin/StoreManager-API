from flask import jsonify
from flask_restful import Resource

from app.api.v1.models import products


class Product(Resource):
    #get single product
    def get(self, id):
        prod = [product for product in products if product['id'] == id]
        return jsonify({"products" : prod})