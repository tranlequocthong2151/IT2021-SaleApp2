from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_admin import Admin
from app.models.models import Category, Product, User
from sqlalchemy import inspect


class ProductView(ModelView):
    column_display_pk = True 
    column_hide_backrefs = False
    column_list = ['id', 'name', 'description', 'price', 'category']


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')



def init_admin(app, db):
    admin = Admin(app, name="Quan ly ban hang",
    template_mode="bootstrap4")
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(StatsView(name='Stats'))
    return admin