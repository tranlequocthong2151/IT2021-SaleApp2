import cloudinary


def init_cloudinary(app):
    cloudinary.config( 
        cloud_name = app.config.get('CLOUDINARY_NAME'), 
        api_key = app.config.get('CLOUDINARY_API_KEY'), 
        api_secret = app.config.get('CLOUDINARY_API_SECRET'), 
    )


    