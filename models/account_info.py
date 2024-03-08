from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String
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
    users = relationship("User", back_populates="account_information", cascade="all, delete-orphan")


    @staticmethod
    def create(command: AccountInfoCmd):
        account_information = AccountInformation()
        account_information.first_name = command.first_name
        account_information.last_name = command.last_name
        account_information.email = command.email
        account_information.password = bcrypt.generate_password_hash(command.get_password()).decode('utf-8')

        return account_information

    def update(self, command):
        self.first_name = command.first_name
        self.last_name = command.last_name
        self.email = command.email
