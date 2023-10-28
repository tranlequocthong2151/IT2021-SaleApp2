from app.dao import product_dao


def get_products(kw=None, category_id=None):
    products = product_dao.get_products()

    if kw:
        products = list(filter(lambda product: product['name'].lower().find(kw.lower()) != -1, products))
    if category_id:
        products = list(filter(lambda product: product['category_id'] == int(category_id), products))

    return products


def get_product(id):
    if not id:
        return None

    return product_dao.get_product(id)
