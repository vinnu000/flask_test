from flask import Blueprint
from flask_restful import Api


accounts_bp = Blueprint('api', __name__, url_prefix='/api')
accounts_api = Api(accounts_bp)

from . import routes

# def register_routes(app):
#     app.register_blueprint(api_blueprint)
