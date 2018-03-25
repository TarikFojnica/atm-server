from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        return "This is Employees"

class Tracks(Resource):
    def get(self):
        return "This is tracks"

class Employees_Name(Resource):
    def get(self):
        return "This is employees name"

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3