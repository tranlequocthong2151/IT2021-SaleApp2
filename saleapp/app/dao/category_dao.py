from app.models.models import Category


def get_categories():
    return Category.query.all()
