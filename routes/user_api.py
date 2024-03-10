from flask import jsonify, request, Blueprint
from sqlalchemy.exc import IntegrityError

from command.user_command import UserCommand
from config.config import db
from dto import AccountInfoDto
from dto import UserInfoDTO
from models.user import User
from services.user_service import UserService


user_controller = Blueprint('main', __name__)


class UserController():
    @user_controller.route('/register', methods=['POST'])
    def register_user():
        try:
            data = request.json
            user_command = UserCommand.create_from_json(data)
            response, status_code = UserService.create_user(user_command)
            return jsonify(response), status_code
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'User with this email already exists'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        
    @user_controller.route('/login', methods=['POST'])
    def login_user():
        data = request.json
        email = data.get('email')
        print(email)
        password = data.get('password')
        print(password)
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        response, status_code = UserService.login(email, password)
        return jsonify(response), status_code
