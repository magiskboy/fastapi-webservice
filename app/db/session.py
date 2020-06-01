# coding=utf-8

from sqlalchemy import create_engine        #type:ignore
from sqlalchemy.orm import (                #type:ignore
    scoped_session,
    sessionmaker,
)
from app import core


engine = create_engine(core.setting.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))
