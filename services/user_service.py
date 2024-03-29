import logging

from sqlalchemy.exc import IntegrityError
from .account_info_service import AccountInfoService
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
        account_info = AccountInfoService.find_by_email(email)

        if account_info and account_info.check_password(password):
            logger.info(f"Login successful for user with email: {email}")
            # generate jwt token
            token = generate_token(email)
            return {'token': token}, 200
        else:
            logger.warning(f"Login failed for email: {email}")
            return {'error': 'Invalid email or password'}, 401