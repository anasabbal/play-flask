from dataclasses import dataclass

from .base_dto import BaseDTO
from models.account_info import AccountInformation

@dataclass
class AccountInfoDto:
    first_name: str
    last_name: str
    email: str
    password: str

    @staticmethod
    def toDto(req: AccountInformation):
        response = AccountInfoDto(
            first_name=req.first_name,
            last_name=req.last_name,
            email=req.email,
            password=req.password
        )
        return response

