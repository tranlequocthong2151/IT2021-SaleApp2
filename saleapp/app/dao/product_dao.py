from app.models import Product


def get_products(kw=None, category_id=None, page=1, page_size=5):
    products = Product.query 
    count = 0

    if kw:
        products = products.filter(Product.name.contains(kw))
    if category_id:
        products = products.filter(Product.category_id == category_id)

    count = products.count()

    page = int(page)
    page_size = int(page_size)
    start = (page - 1) * page_size
    products = products.offset(start).limit(page_size)

    return {
        "products": products.all(),
        "count": count
    }


def get_product(id):
    return Product.query.get(int(id))
