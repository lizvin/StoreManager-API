from flask import jsonify, request
from flask_restful import Resource

from app.api.v1.models import sales_orders

class Sale_order(Resource):
    #get single sale order
    def get(self, id):
        sale_order = [order for order in sales_orders if order['id'] == id]
        return jsonify({"products" : sale_order})