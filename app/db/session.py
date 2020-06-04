# coding=utf-8

import logging
import time
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from app import core


RUNTIME_LOGGER = logging.getLogger('sqlalchemy.runtime')

engine = create_engine(core.setting.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))


def before_cursor_execute(conn, cursor, statement, params, context, execmany):      # pylint: disable=W0613,R0913
    conn.info.setdefault('query_start_time', []).append(time.time())


def after_cursor_execute(conn, cursor, statement, params, context, execmany):       # pylint: disable=W0613,R0913
    total = time.time() - conn.info['query_start_time'].pop(-1)
    if total > core.setting.QUERY_TIME_THRESHOLD:
        RUNTIME_LOGGER.debug(f' SLOW QUERY: {total:.3f} '.center(80, '-'))
        RUNTIME_LOGGER.debug(f'Params: {params}')       # pylint: disable=W1202
        RUNTIME_LOGGER.debug(statement)


def enable_time_logging():
    RUNTIME_LOGGER.setLevel(logging.DEBUG)
    event.listens_for(Engine, 'before_cursor_execute')(before_cursor_execute)
    event.listens_for(Engine, 'after_cursor_execute')(after_cursor_execute)
