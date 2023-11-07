from flask import Flask, render_template, request, redirect, session, jsonify
from flask_mail import Mail, Message
from flask_login import LoginManager

from config import Config
from app.extensions import db 
from app.admin import init_admin
from app.services import product_service
from app.services import category_service
from app.services import user_service
from app.services import token_service
from app.decorators.auth import signin_required


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    mail = Mail(app)

    db.init_app(app)

    init_admin(app, db)

    login = LoginManager(app)

    manage_services = {
        'categories': category_service.get_categories,
        'users': user_service.get_users,
        'products': product_service.get_products,
    }

    @login.user_loader
    def load_user(user_id):
        return user_service.get_user(user_id)


    @app.context_processor
    def inject_categories():
        return dict(categories=category_service.get_categories(), user=session['user'] if 'user' in session else None)


    @app.get("/")
    def home():
        products = product_service.get_products()

        return render_template('products.html', products=products)


    @app.get("/products")
    def product_list():
        category_id = request.args.get('category_id')
        kw = request.args.get('kw')

        products = product_service.get_products(kw=kw, category_id=category_id)

        return render_template('products.html', products=products)


    @app.get("/products/<product_id>")
    def product_detail(product_id):
        product = product_service.get_product(product_id)

        return render_template('product.html', product=product)


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application</h1>'


    @app.get('/profile')
    def profile_page():
        if 'user' in session:
            return render_template('profile.html', user=session['user'])
        else:
            return redirect('/')


    @app.get('/signout')
    def signout():
        if 'user' in session:
            session.pop('user')
        return redirect('/')


    @app.get('/signin')
    def signin_page():
        if 'user' in session:
            return redirect('/')
        else:
            return render_template('signin.html')


    @app.post('/signin')
    def signin():
        username = request.form.get('username')
        password = request.form.get('password')

        user = user_service.signin(username=username, password=password)
        user = jsonify(user)

        if user:
            session['user'] = user[0]
            return redirect('/')
        else:
            return render_template('signin.html', message='Sai tên tài khoản hoặc mật khẩu, xin vui lòng thử lại.')


    @app.get('/signup')
    def signup_page():
        if 'user' in session:
            return redirect('/')
        else:
            return render_template('signup.html')


    @app.post('/signup')
    def signup():
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        avatar = request.form.get('avatar')

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

    return app
