# coding=utf-8

from typing import (
    Optional,
    Dict,
    Any,
)
from sqlalchemy.engine.url import URL
from pydantic import (
    BaseSettings,
    validator
)


class Setting(BaseSettings):
    SERVICE_NAME: str = 'FastAPI service'
    DEBUG: bool = False
    SENTRY_DSN: Optional[str] = None

    QUERY_TIME_THRESHOLD: float = 0.05
    DB_DRIVE: str = 'sqlite'
    DB_HOST: str = None
    DB_PORT: int = None
    DB_USER: str = None
    DB_PASS: str = None
    DB_NAME: str = ':memory:'
    SQLALCHEMY_DATABASE_URI: str = ''
    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def build_db_uri(cls, value: Optional[str], values: Dict[str, Any]) -> Any:        # pylint: disable=R0201,E0213
        if bool(value):
            return value
        url = URL(
            drivername=values.get('DB_DRIVE', str(values)),
            username=values.get('DB_USER'),
            password=values.get('DB_PASS'),
            host=values.get('DB_HOST'),
            port=values.get('DB_PORT'),
            database=values.get('DB_NAME')
        )
        return str(url)


setting = Setting()
