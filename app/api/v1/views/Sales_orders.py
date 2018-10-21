from flask import jsonify, request
from flask_restful import Resource
from app.api.v1.models import sales_orders


class Sales_orders(Resource):
    #get all sales orders
    def get(self):
        return jsonify({ "message":"Sales orders successfully fetched", "sales_orders" : sales_orders })
    
    #post a sale order
    def post(self):
        data = request.get_json()
        id  = len(sales_orders) + 1
        name = data['name']
        price = data['price']
        category = data['category']

        new_sale_order = {
            "id" : id,
            "Description" : {
                "name" : name,
                "price" : price,
                "category" : category
            }
        }

        sales_orders.append(new_sale_order)

        return jsonify({ "message":"Product successfully added", "sales_orders" : sales_orders })
