from dataclasses import dataclass
from dto import BaseDTO
from models.account_info import AccountInformation


@dataclass
class AccountInfoDto(BaseDTO):
    first_name : str
    last_name :str
    email : str
    password : str

    @staticmethod
    def toDto(req: AccountInformation):
        response = AccountInfoDto()

        response.first_name = req.first_name
        response.last_name = req.last_name
        response.email = req.email
        response.password = req.password

        return response

