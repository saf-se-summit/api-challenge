from flask import jsonify 
from flask_restful import Resource
from database import Customer 

class Customer(Resource):

    def get(self):
        pass

    def put(self):
        pass 

    def delete(self):
        pass 


class CustomerList(Resource):

    def get(self):
        customers = Customer.query.all()
        return jsonify(customers)

    def post(self):
        pass 