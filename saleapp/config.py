import os

from urllib.parse import quote


class Config:
    password = os.environ.get('DATABASE_PASSWORD')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/saledb?charset=utf8mb4' % quote(password) 
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')

    ITD_KEY=os.environ.get('ITD_KEY')
    ITD_SALT=os.environ.get('ITD_SALT')
