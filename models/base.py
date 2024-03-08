import uuid

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql import func
from config.config import db

Base = declarative_base()

@declarative_mixin
class BaseEntity(Base ,db.Model):

    __abstract__ = True


    id = Column(String, primary_key=True, default=uuid.uuid4())
    version = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    created_by = Column(String, default="NAS_SYSTEM")
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_by = Column(String, "NAS_SYSTEM")
    deleted = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
