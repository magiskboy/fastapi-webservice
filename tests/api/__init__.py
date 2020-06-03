# coding=utf-8

import pytest
from starlette.testclient import TestClient
from fastapi import FastAPI
from tests import BaseTestCase


@pytest.mark.usefixtures('api')
class APITestCase(BaseTestCase):
    app: FastAPI
    client: TestClient
