from functools import wraps
from flask import session, redirect, request, url_for


def signin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('signin_page', next=request.url))
        else:
            return f(*args, **kwargs)

    return wrapper

