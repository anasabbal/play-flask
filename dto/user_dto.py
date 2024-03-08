from dataclasses import dataclass
from typing import List
from dto import BaseDTO
from dto import AccountInfoDto
from models.client_type import ClientType


@dataclass
class UserInfoDTO(BaseDTO):

    account_info: List[AccountInfoDto]
    client_type: ClientType