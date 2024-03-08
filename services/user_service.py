import logging

from sqlalchemy.exc import IntegrityError

from config.config import db
from models.account_info import AccountInformation
from models.user import User
from utils.jwt_config import generate_token
from utils.validate import validate_email

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserService():

    # function to create user
    @staticmethod
    def create_user(cmd: AccountInformation):
        try:
            validate_email(cmd.get_email())
            user = User.create(cmd)
            print(user)
            user.save()
            logger.info('User created successfully')
            return {'message': 'User created successfully'}, 201
        except IntegrityError:
            db.session.rollback()
            logger.error('User creation failed: User with this email already exists')
            return {'error': 'User with this email already exists'}, 400
        except Exception as e:
            db.session.rollback()
            logger.exception('User creation failed: %s', str(e))
            return {'error': 'User creation failed'}, 500
    
    # login user
    @staticmethod
    def login(email: str, password: str):
        # find user by email
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # generate jwt token
            token = generate_token(user.id)
            return {'token': token}, 200
        else:
            return {'error': 'Invalid email or password'}, 401