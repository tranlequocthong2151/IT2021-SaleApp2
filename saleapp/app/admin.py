from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_admin import Admin
from flask_login import logout_user, current_user
from flask import redirect

from app import app, db
from app.models import Category, Product, User, UserRole


class PrivateView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class StatsView(PrivateView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


class SignoutView(PrivateView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


class PrivateModelView(ModelView, PrivateView):
    column_display_pk = True 
    column_hide_backrefs = False
    column_searchable_list = ['name']
    column_filters = ['name']
    can_export = True
    can_view_details = True


class ProductView(PrivateModelView):
    column_list = ['id', 'name', 'description', 'price', 'category']


class CategoryView(PrivateModelView):
    column_list = ['id', 'name', 'products']


class SalesPage(BaseView):
    @expose('/')
    def index(self):
        return redirect('/')



admin = Admin(app, name="Quan ly ban hang", template_mode="bootstrap4")
admin.add_view(SalesPage(name='Sales'))
admin.add_view(CategoryView(Category, db.session))
admin.add_view(PrivateModelView(User, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name='Stats'))
admin.add_view(SignoutView(name='Signout'))
