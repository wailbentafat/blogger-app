
from flask import Flask
from flask_login import  LoginManager
'''from app''' 
import routes, models, forms
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# @login_manager.user_loader 
login_manager = LoginManager()


login_manager.init_app(app)