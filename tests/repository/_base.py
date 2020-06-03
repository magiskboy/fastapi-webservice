# coding=utf-8

from tests import BaseTestCase


class RepositoryTestCase(BaseTestCase):
    __repoclass__: type
    __args__: tuple = ()
    __kwargs__: dict = {}

    def __init__(self, *args, **kwargs):
        cls = self.__class__
        super().__init__(*args, **kwargs)
        self.repo = cls.__repoclass__(*cls.__args__, **cls.__kwargs__)
