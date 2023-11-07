from app.models.models import User
from app.extensions import db


def get_user(username='', password='', email=''):
    user = User.query
    if username:
        user = user.filter(User.username == username)
    if password:
        user = user.filter(User.password == password)
    if email:
        user = user.filter(User.email == email)
    return user.all()[0] if user.all()[0] else None


def get_users():
    return User.query.all()


def add_user(full_name, username, email, password, avatar):
    user = User(name=full_name, email=email, username=username, password=password, avatar=avatar)
    db.session.add(user)
    db.session.commit()
    return user


def add_user_by_obj(user):
    db.session.add(user)
    db.session.commit()
    return True
