from sqlalchemy import Integer, String, Column, ForeignKey, Float, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_login import UserMixin

import enum

from app import db


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    description = Column(String(100))
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


class UserRole(enum.IntEnum):
    USER = 0
    ADMIN = 1


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=False)
    avatar = Column(String(255))
    joined_date = Column(DateTime, server_default=func.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


# if __name__ == '__main__':
#     from app import app, db
#     with app.app_context():
#         db.create_all()

#         import hashlib
#         # u = User(name='Admin', email="admin@gmail.com", username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), user_role=UserRole.ADMIN)
#         # db.session.add(u)
#         # db.session.commit()
#         # u = User(name='Admin 2', email="admin2@gmail.com", username='admin2', avatar="https://res.cloudinary.com/diojasks1/image/upload/v1651031632/cld-sample.jpg", password=str(hashlib.md5('2525'.encode('utf-8')).hexdigest()), user_role=UserRole.ADMIN)
#         # db.session.add(u)
#         # db.session.commit()
#         u = User(name='Admin 3', email="admin3@gmail.com", username='admin3', avatar="https://res.cloudinary.com/diojasks1/image/upload/v1651031632/cld-sample.jpg", password=str(hashlib.md5('2525'.encode('utf-8')).hexdigest()), user_role=UserRole.ADMIN)
#         db.session.add(u)
#         db.session.commit()
        
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        # p1 = Product(name='iPad Pro 2022', price=24000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg")
        # p2 = Product(name='iPhone 13', price=21000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg")
        # p3 = Product(name='Galaxy S23', price=24000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg")
        # p4 = Product(name='Note 22', price=22000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg")
        # p5 = Product(name='Galaxy Tab S9', price=24000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg")
        # p6 = Product(name='iPad Pro 2023', price=24000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg")
        # p7 = Product(name='iPhone 15 Pro', price=21000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg")
        # p8 = Product(name='Galaxy S24', price=24000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg")
        # p9 = Product(name='Note 23 Pro', price=22000000, category_id=1,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg")
        # p10 = Product(name='Galaxy Tab S9 Ultra', price=24000000, category_id=2,
        #              image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1691062682/tkeflqgroeil781yplxt.jpg")

        # # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.add_all([p6, p7, p8, p9, p10])
        # db.session.commit()
