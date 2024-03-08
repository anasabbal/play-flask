import logging
from command.user_command import UserCommand
from models.user import User
from sqlalchemy.exc import IntegrityError
from config.config import db
from utils.jwt_config import generate_token
from utils.validate import validate_email

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserService():

    # function to create user
    @staticmethod
    def create_user(user_command: UserCommand):
        try:
            validate_email(user_command.get_email())
            user = User.create(user_command)
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
    def login(email, password):
        # find user by email
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # generate jwt token
            token = generate_token(user.id)
            return {'token': token}, 200
        else:
            return {'error': 'Invalid email or password'}, 401