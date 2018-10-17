from flask import make_response, jsonify, request
from flask_restful import Api, Resource

from cart import cart

class Cart(Resource):
   def get(self):
       return make_response(jsonify(
           {
               'Products':cart
           }
       ), 200)

   def post(self):
       data = request.get_json()
       name = data['name']
       price = data['price']

       items = {
           'name':name,
           'price':price
       }

       return make_response(jsonify(
           {
               'Pro':items
           }
       ), 200)
