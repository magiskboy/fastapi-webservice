# coding=utf-8

import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from app import (
    core,
    api,
)


sentry_sdk.init(
    dsn=core.setting.SENTRY_DSN,
    integrations=[SqlalchemyIntegration()]
)
app = api.create_asgi()
app = SentryAsgiMiddleware(app)
