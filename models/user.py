from sqlalchemy import Column, String
from config.config import db
from command.user_command import UserCommand
import uuid
import logging
import app
from flask_bcrypt import Bcrypt 



bcrypt = Bcrypt() 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=uuid.uuid4())
    first_name = Column(String(10), nullable=False)
    last_name = Column(String(10), nullable=False)
    email = Column(String(120), unique=True)
    password = Column(String(255), nullable=False)


    # function to create user from command
    @classmethod
    def create(cls, user_command: UserCommand):
        hashed_password = bcrypt.generate_password_hash(user_command.get_password()).decode('utf-8')
        user = cls(
            first_name=user_command.get_first_name(),
            last_name=user_command.get_last_name(),
            email=user_command.get_email(),
            password=hashed_password
        )

        return user
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            "last_name": self.last_name,
            'email': self.email,
            'password': self.password
        }
    
    # check password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)