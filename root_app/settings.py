from root_app import app
from flask_sqlalchemy import SQLAlchemy


app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)
