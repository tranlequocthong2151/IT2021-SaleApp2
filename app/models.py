from sqlalchemy import Integer, String, Column
from flask_sqlalchemy import SQLAlchemy

from app import app


db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)


if __name__ == '__main__':
    from app import app

    with app.app_context():
        db.create_all() 