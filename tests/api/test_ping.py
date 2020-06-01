# coding=utf-8

from tests.api import APITestCase

class TestPing(APITestCase):
    def test_ping(self):
        res = self.client.get('/health')
        assert 204 == res.status_code
