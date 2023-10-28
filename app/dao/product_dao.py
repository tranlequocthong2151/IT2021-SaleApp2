from app.utils import read_json_file


def get_products():
    return read_json_file('products') 


def get_product(id):
    products = read_json_file('products') 

    for product in products:
        if product['id'] == int(id):
            return product
    
    return None
