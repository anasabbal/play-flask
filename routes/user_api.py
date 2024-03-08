from flask import jsonify, request, Blueprint
from sqlalchemy.exc import IntegrityError
from models.user import User
from command.user_command import UserCommand
from services.user_service import UserService
from config.config import db


user_controller = Blueprint('main', __name__)
user_service = UserService()


class UserController():

    @user_controller.route('/users', methods=['GET'])
    def get_users():
        try:
            users = User.query.all()
            user_list = [{
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'password': user.password
            } for user in users]
            return jsonify(user_list), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @user_controller.route('/register', methods=['POST'])
    def register_user():
        try:
            data = request.json
            user_command = UserCommand.create_from_json(data)
            response, status_code = user_service.create_user(user_command)
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
        response, status_code = user_service.login(email, password)
        return jsonify(response), status_code
