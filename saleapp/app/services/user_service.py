from app.dao import user_dao
import hashlib


def signin(username=None, password=None):
    if not username or not password:
        return 

    return user_dao.get_user(username=username, password=password)


def get_users():
    return user_dao.get_users()


def get_user(email):
    return user_dao.get_user(email=email)


def add_user(user):
    return user_dao.add_user_by_obj(user)


def signup(full_name, username, email, password, avatar):
    if not full_name or not username or not email or not password:
        raise ValueError('Empty input')

    password = hashlib.md5(password.encode()).hexdigest()
    return user_dao.add_user(full_name=full_name, username=username, email=email, password=password, avatar=avatar)

