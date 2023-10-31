from flask import render_template, request

from app.services import product_service
from app import app


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


if __name__ == '__main__':
    app.run(debug=True)