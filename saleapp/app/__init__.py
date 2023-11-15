from dotenv import load_dotenv

load_dotenv()

from flask import Flask 
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
from app.extensions import init_cloudinary


app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

db = SQLAlchemy(app)

init_cloudinary(app)

login = LoginManager(app)
login.login_view = 'signin'

from app import routes, admin
