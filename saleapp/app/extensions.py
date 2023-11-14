import os

from flask_sqlalchemy import SQLAlchemy
import cloudinary


db = SQLAlchemy()
          

def init_cloudinary():
    cloudinary.config( 
        cloud_name = os.environ.get('CLOUDINARY_NAME'), 
        api_key = os.environ.get('CLOUDINARY_API_KEY'), 
        api_secret = os.environ.get('CLOUDINARY_API_SECRET'), 
    )


    