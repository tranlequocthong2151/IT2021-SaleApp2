import os 
from urllib.parse import quote

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    password = os.getenv('DATABASE_PASSWORD')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/saledb?charset=utf8mb4' % quote(password) 
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')

    ITD_KEY=os.getenv('ITD_KEY')
    ITD_SALT=os.getenv('ITD_SALT')
    

