# coding=utf-8

from sqlalchemy.ext.declarative import (
    as_declarative,
    declared_attr
)
from sqlalchemy import (
    Column,
    Integer
)


@as_declarative()
class Base:
    id_ = Column('id', Integer(), primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:      # pylint: disable=E0213
        return cls.__name__.lower()     # pylint: disable=E1101
