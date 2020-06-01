# coding=utf-8

import pytest
from starlette.testclient import TestClient
from app import api as api_module


@pytest.fixture
def api(request):
    app = None
    if request.cls is not None:
        app = api_module.create_asgi()
        request.cls.app = app
        request.cls.client = TestClient(app)
    yield app
