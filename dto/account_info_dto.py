from dataclasses import dataclass

from .base_dto import BaseDTO
from models.account_info import AccountInformation

@dataclass
class AccountInfoDto(BaseDTO):
    first_name: str
    last_name: str
    email: str
    password: str

    @staticmethod
    def toDto(req: AccountInformation):
        response = AccountInfoDto(
            id=req.id,
            version=req.version,
            created_at=str(req.created_at),
            created_by=req.created_by,
            updated_at=str(req.updated_at),
            updated_by=req.updated_by,
            deleted=req.deleted,
            active=req.active,
            first_name=req.first_name,
            last_name=req.last_name,
            email=req.email,
            password=req.password
        )
        return response

