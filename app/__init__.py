from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship


app = Flask(__name__)

db_password = 'Admin@123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4' % quote(db_password)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


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
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all() 

        # db.session.add(Category(name='Mobile'))
        # db.session.add(Category(name='Tablet'))
        
        # db.session.commit()

        # db.session.add(Product(name='IPhone 15', price=2000, image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg', category_id=1))
        # db.session.add(Product(name='Ipad Pro', price=2400, image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg', category_id=2))

        # db.session.commit()

        app.run(debug=True)