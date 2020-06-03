# coding=utf-8

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app import core
from . import v1


def create_asgi() -> FastAPI:
    app = FastAPI(
        title=core.setting.SERVICE_NAME,
        debug=core.setting.DEBUG,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1.api_router, prefix='/v1')

    return app
