# coding=utf-8

from unittest.mock import patch
from app import core
from tests import BaseTestCase


class CoreTestCase(BaseTestCase):
    def test_seting(self):
        db_uri = core.setting.SQLALCHEMY_DATABASE_URI
        assert db_uri.startswith('sqlite:///')

    def test_mysql_dialect(self):
        env = {
            'DB_DRIVE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_PORT': '3306',
            'DB_USER': 'username',
            'DB_PASS': 'pass',
            'DB_NAME': 'dbname'
        }
        with patch.dict('os.environ', env) as mock_env:
            setting = core.config.Setting()
            db_uri = setting.SQLALCHEMY_DATABASE_URI
            assert f'{env["DB_DRIVE"]}://{env["DB_USER"]}:{env["DB_PASS"]}@{env["DB_HOST"]}:{env["DB_PORT"]}/{env["DB_NAME"]}' == db_uri

    def test_buildin_uri(self):
        env = {
            'SQLALCHEMY_DATABASE_URI': 'mysql:///user:pass@local:3306/db'
        }
        with patch.dict('os.environ', env) as mock_env:
            setting = core.config.Setting()
            db_uri = setting.SQLALCHEMY_DATABASE_URI
        assert env['SQLALCHEMY_DATABASE_URI'] == db_uri
