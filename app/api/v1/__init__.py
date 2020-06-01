# coding=utf-8

from fastapi import APIRouter


api_router = APIRouter()


@api_router.get('/ping')
def ping() -> str:
    return 'pong'
