# coding=utf-8

from typing import Optional
from pydantic import BaseSettings



class Setting(BaseSettings):
    SERVICE_NAME: str = 'FastAPI service'
    SQLALCHEMY_DATABASE_URI: Optional[str] = 'sqlite:///:memory:'
    DEBUG: bool = False
    SENTRY_DSN: Optional[str] = None


setting = Setting()
