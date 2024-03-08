import os
from datetime import datetime, timedelta

import jwt
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    # Access SECRET_KEY from environment variables
    secret_key = os.getenv('SECRET_KEY')
    return jwt.encode(payload, secret_key, algorithm='HS256')