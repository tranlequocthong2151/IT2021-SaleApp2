from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey, Float, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.extensions import db


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    description = Column(String(100))
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


class UserRole(enum.IntEnum):
    USER = 0
    ADMIN = 1


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String(100))
    joined_date = Column(DateTime, server_default=func.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)


