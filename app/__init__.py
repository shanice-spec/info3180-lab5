from flask import Flask
from .config import Config
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)
migrate = Migrate(app, db) 

from app import views