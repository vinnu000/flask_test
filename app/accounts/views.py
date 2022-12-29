from flask import jsonify
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return jsonify(username='vinod', email='vinodkumar.t@dvara.com')
