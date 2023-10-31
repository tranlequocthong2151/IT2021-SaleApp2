from app.dao import category_dao


def get_categories():
    return category_dao.get_categories()
