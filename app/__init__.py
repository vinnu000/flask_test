from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "dev"])
    api = Api(app)

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
