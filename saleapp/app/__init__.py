from flask import Flask, render_template, request

from config import Config
from app.extensions import db
from app.services import product_service
from app.services import category_service


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)


    @app.context_processor
    def inject_categories():
        return dict(categories=category_service.get_categories())


    @app.get("/")
    def home():
        products = product_service.get_products()

        return render_template('products.html', products=products)


    @app.get("/products")
    def product_list():
        category_id = request.args.get('category_id')
        kw = request.args.get('kw')

        products = product_service.get_products(kw=kw, category_id=category_id)

        return render_template('products.html', products=products)


    @app.get("/products/<product_id>")
    def product_detail(product_id):
        product = product_service.get_product(product_id)

        return render_template('product.html', product=product)


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application</h1>'


    return app
