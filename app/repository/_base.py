# coding=utf-8

import typing as T
from pydantic import BaseModel      # pylint: disable=E0611
from fastapi.encoders import jsonable_encoder
from app.db import (
    Base as DbBaseModel,
    Session,
)


class CRUDBase:
    def __init__(self, model: DbBaseModel):
        self.model: DbBaseModel = model

    def get(self, oid: int) -> T.Union[DbBaseModel, None]:
        return Session.query(self.model).get(oid)

    def get_multi(self, offset: int = 0, limit: int = 10,
                  lazy: bool = True) -> T.List[DbBaseModel]:
        query = Session.query(self.model).offset(offset).limit(limit)
        if lazy:
            return query
        return query.all()

    def create(self, data: T.Union[dict, BaseModel]) -> DbBaseModel:
        if isinstance(data, BaseModel):
            data = jsonable_encoder(data)
        obj = self.model(**data)
        Session.add(obj)
        Session.commit()
        return obj

    @staticmethod
    def update(obj: DbBaseModel,
               data: T.Union[dict, BaseModel]) -> DbBaseModel:
        if isinstance(data, BaseModel):
            data = jsonable_encoder(data)
        for attribute, value in data.items():
            if hasattr(obj, attribute):
                setattr(obj, attribute, value)
        Session.commit()
        return obj

    @staticmethod
    def delete(obj: DbBaseModel) -> T.NoReturn:
        Session.delete(obj)
        Session.commit()
