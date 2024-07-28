import jwt
from datetime import datetime, timedelta
from flask import current_app

def create_token(key, time):

    token = jwt.encode(
            {
            'key' : key,
            'exp' : datetime.utcnow() + timedelta(minutes = time)
            },
            key = current_app.config['SECRET_KEY'],
            algorithm = 'HS512',
        )
    
    return token