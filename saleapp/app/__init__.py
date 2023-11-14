from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, session
from flask_mail import Mail, Message
from flask_login import login_user, current_user, LoginManager, logout_user, login_required
from flask_restful import Resource, Api
import cloudinary.uploader
import uuid

from config import Config
from app.extensions import db, init_cloudinary
from app.admin import init_admin
from app.services import product_service
from app.services import category_service
from app.services import user_service
from app.services import token_service
from app.models.models import UserRole


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    mail = Mail(app)

    db.init_app(app)

    init_cloudinary()

    init_admin(app, db)

    login = LoginManager(app)
    login.login_view = 'signin'

    manage_services = {
        'categories': category_service.get_categories,
        'users': user_service.get_users,
        'products': product_service.get_products,
    }


    @app.get('/carts')
    def cart_page():
        products = []
        if session['cart']:
            for id in session['cart']:
                product = product_service.get_product(int(id))
                if product:
                    product.quantity = session['cart'][id]
                    products.append(product)
        amount = 0
        for product in products:
            amount += product.price
        return render_template('cart.html', products=products, amount=amount)


    @app.post('/carts/<product_id>')
    def add_to_cart(product_id):
        id = str(product_id)
        if 'cart' not in session:
            session['cart'] = {}

        if id in session['cart']:
            session['cart'][id] += 1
        else: 
            session['cart'][id] = 1
        session.modified = True
        return redirect('/products')


    @login.user_loader
    def load_user(user_id):
        return user_service.get_user(id=user_id)


    @app.context_processor
    def inject_categories():
        return dict(categories=category_service.get_categories(), user=current_user)


    @app.get("/")
    @login_required
    def home():
        products = product_service.get_products()

        return render_template('products.html', products=products)


    @app.get("/products")
    @login_required
    def product_list():
        category_id = request.args.get('category_id')
        kw = request.args.get('kw')

        products = product_service.get_products(kw=kw, category_id=category_id)

        return render_template('products.html', products=products)


    @app.get("/products/<product_id>")
    @login_required
    def product_detail(product_id):
        product = product_service.get_product(product_id)

        return render_template('product.html', product=product)



    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application</h1>'


    @app.get('/profile')
    @login_required
    def profile_page():
        return render_template('profile.html', user=current_user)


    @app.get('/signout')
    @login_required
    def signout():
        logout_user()
        return redirect('/signin')


    @app.get('/signin')
    def signin_page():
        if current_user.is_authenticated:
            return redirect('/')
        else:
            return render_template('signin.html')


    @app.post('/signin')
    def signin():
        username = request.form.get('username')
        password = request.form.get('password')

        user = user_service.signin(username=username, password=password)

        if user:
            login_user(user=user)
            return redirect('/')
        else:
            return render_template('signin.html', message='Sai tên tài khoản hoặc mật khẩu, xin vui lòng thử lại.')


    @app.get('/signup')
    def signup_page():
        if current_user.is_authenticated:
            return redirect('/')
        else:
            return render_template('signup.html')


    @app.post('/signup')
    def signup():
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        avatar = request.files.get('avatar')

        avatar = cloudinary.uploader.upload(avatar, public_id=str(uuid.uuid4()))['url']

        try:
            user_service.signup(full_name=full_name, username=username, email=email, password=password, avatar=avatar)
        except Exception as e:
            print(e)
            return render_template('signup.html', message='Có lỗi xảy ra, xin vui lòng thử lại.')

        token = token_service.generate_token(key=app.config.get('ITD_KEY'), salt=app.config.get('ITD_SALT'), email=email)

        msg = Message('Xác thực tài khoản', recipients=[email])
        msg.body = f'Chào {full_name},\n\nĐây là mail xác thực đăng ký tài khoản tại trang web bán hàng trực tuyến\n\nVui lòng nhấp vào link này để xác thực: {request.url_root + "confirm/" + token}\n\nLink sẽ hết hạn sau 1 tiếng\n\n\nTrân trọng,\nBán hàng trực tuyến'

        mail.send(msg)
        return render_template('signup.html', message="Bạn đã đăng ký thành công, vui lòng truy cập vào mail để xác thực tài khoản trước khi có thể sử dụng.")


    @app.get('/confirm/<token>')
    def confirm_signup(token):
        email = token_service.confirm_token(key=app.config.get('ITD_KEY'), salt=app.config.get('ITD_SALT'), token=token)
        if email:
            user = user_service.get_user(email=email)
            user.active = True
            actived = user_service.add_user(user=user)
        else:
            print('Invalid')

        if actived:
            return redirect('/signin')
        else:
            return '<h1>Error occurred</h1>'


    @app.post('/admin/signin')
    def admin_signin():
        username = request.form.get('username')
        password = request.form.get('password')

        user = user_service.signin(username=username, password=password)

        if user and user.user_role == UserRole.ADMIN:
            login_user(user=user)
        return redirect('/admin')

    return app
