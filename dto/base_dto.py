from dataclasses import dataclass

@dataclass
class BaseDTO:
    id: str
    version: int
    created_at: str
    created_by: str
    updated_at: str
    updated_by: str
    deleted: bool
    active: bool
