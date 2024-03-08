import logging

from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from command.account_info_cmd import AccountInfoCmd
from config.config import db
from models import BaseEntity, ClientType, AccountInformation

bcrypt = Bcrypt()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseEntity):
    __tablename__ = 'users'

    account_information_id = Column(String, ForeignKey('account_information.id'))
    account_information = relationship("AccountInformation", back_populates="users")
    client_type = Column(Enum(ClientType), default=ClientType.PERSON)
    is_enabled = Column(Boolean, default=False)
    

    # function to create user from command
    @staticmethod
    def create_and_save(account_information: AccountInformation):
        user = User()
        user.account_information = account_information
        return user
    
    @staticmethod
    def create(cmd: AccountInfoCmd):
        payload : AccountInformation = AccountInformation.create(cmd)
        return User.create_and_save(payload)
    
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