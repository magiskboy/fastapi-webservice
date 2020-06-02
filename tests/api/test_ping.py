# coding=utf-8

from tests.api import APITestCase

class TestPing(APITestCase):
    def test_ping(self):
        res = self.client.get('/v1/ping')
        assert 200 == res.status_code
        assert '"pong"' == res.text
