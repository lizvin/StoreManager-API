from flask import Flask
from flask_restful import Api

from app.api.v1.views.products import Cart

app=Flask(__name__)

api=Api(app)

api.add_resource(Cart, "/api/v1/views/products")
