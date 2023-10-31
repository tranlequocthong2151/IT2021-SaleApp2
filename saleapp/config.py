import os

from urllib.parse import quote


class Config:
    password = os.environ.get('DATABASE_PASSWORD')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/saledb?charset=utf8mb4' % quote(password) 
    SQLALCHEMY_TRACK_MODIFICATIONS = True


