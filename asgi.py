# coding=utf-8

import os
import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from app import (
    core,
    api,
)


app = api.create_asgi()

ENABLE_SENTRY = os.getenv('ENABLE_SENTRY', 'false')
if ENABLE_SENTRY == 'true':
    sentry_sdk.init(
        dsn=core.setting.SENTRY_DSN,
        integrations=[SqlalchemyIntegration()]
    )
    app = SentryAsgiMiddleware(app).app
