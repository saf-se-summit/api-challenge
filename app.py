import os
from flask import Flask 
from flask_restful import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from resources import *

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

api.add_resource(Customer, "customer/<str:id>")
api.add_resource(CustomerList, "customer/")


if __name__ == '__main__':
    app.run(debug=True)