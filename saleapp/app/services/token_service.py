from itsdangerous import URLSafeTimedSerializer


def generate_token(key, salt, email):
    serializer = URLSafeTimedSerializer(key)
    return serializer.dumps(email, salt=salt)


def confirm_token(key, salt, token, expiration=3600):
    serializer = URLSafeTimedSerializer(key)
    try:
        email = serializer.loads(
            token, salt=salt, max_age=expiration
        )
        return email
    except Exception:
        return None
