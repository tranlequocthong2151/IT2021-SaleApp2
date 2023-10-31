from app.dao import product_dao


def get_products(kw=None, category_id=None):
    products = product_dao.get_products(kw=kw, category_id=category_id)

    return products


def get_product(id):
    if not id:
        return None

    return product_dao.get_product(id)
