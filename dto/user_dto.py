from dataclasses import dataclass
from typing import List
from dto import BaseDTO
from dto import AccountInfoDto
from models.client_type import ClientType


@dataclass
class UserInfoDTO(BaseDTO):

    account_info: List[AccountInfoDto]
    client_type: ClientType

    def __init__(self, id: str, version: int, created_at: str, created_by: str,
                 updated_at: str, updated_by: str, deleted: bool, active: bool,
                 account_info: List[AccountInfoDto], client_type: ClientType):
        super().__init__(id=id, version=version, created_at=created_at,
                         created_by=created_by, updated_at=updated_at,
                         updated_by=updated_by, deleted=deleted, active=active)
        self.account_info = account_info
        self.client_type = client_type