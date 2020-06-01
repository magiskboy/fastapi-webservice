# coding=utf-8

from app import db
from tests import BaseTestCase


class BaseModelTestCase(BaseTestCase):
    def setUp(self):
        class Product(db.Base):
            pass
        self.model_cls = Product

    def test_class_model_config(self):
        assert self.model_cls.__tablename__ == self.model_cls.__name__.lower()
        assert hasattr(self.model_cls, 'id_')
