# coding=utf-8

import fastapi
from starlette.middleware.cors import CORSMiddleware
from app import core
from app.api import v1


def create_asgi() -> fastapi.FastAPI:
    """Function facetory for create a new ASGI object"""
    app = fastapi.FastAPI(
        title=core.setting.SERVICE_NAME,
        debug=core.setting.DEBUG,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/health')
    async def health():       #pylint: disable=W0612
        return fastapi.Response('', 204)

    app.include_router(v1.api_router, prefix='/v1')

    return app
