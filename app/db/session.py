# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import core


engine = create_engine(core.setting.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
