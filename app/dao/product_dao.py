from app import Product


def get_products(kw=None, category_id=None):
    products = Product.query 

    if kw:
        products = Product.query.filter(Product.name.contains(kw))
    if category_id:
        products = Product.query.filter(Product.category_id == category_id)

    return products.all()


def get_product(id):
    return Product.query.get(id=int(id))