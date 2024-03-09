from typing import Self
from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from command.account_info_cmd import AccountInfoCmd
from models.base import BaseEntity

bcrypt = Bcrypt()



class AccountInformation(BaseEntity):
    __tablename__ = 'account_information'

    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    password = Column(String)
    user = relationship("User", back_populates="account_information")
    
    @classmethod
    def create(cls, command: AccountInfoCmd):
        acc = cls()
        acc.first_name = command.first_name
        acc.last_name = command.last_name
        acc.email = command.email
        acc.password = bcrypt.generate_password_hash(command.get_password()).decode('utf-8')
        return cls

    def update(self, command):
        self.first_name = command.first_name
        self.last_name = command.last_name
        self.email = command.email

    # check password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
