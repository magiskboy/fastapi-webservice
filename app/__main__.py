# coding=utf-8

import click
import uvicorn      #type:ignore
import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from app import (
    core,
    api,
)


app = api.create_asgi()


def run_server(host='0.0.0.0', port=8000, workers=None,     #pylint:disable=R0913
               reload=False, log_level='error', loop='uvloop',
               enable_sentry=False):
    global app      #pylint:disable=W0603,C0103

    if enable_sentry:
        sentry_sdk.init(
            dsn=core.setting.SENTRY_DSN,
            integrations=[SqlalchemyIntegration()]
        )
        app = SentryAsgiMiddleware(app).app

    uvicorn.run('app.__main__:app', host=host, port=port, reload=reload, \
                workers=workers, log_level=log_level, loop=loop)


def show_routes():
    global app      #pylint:disable=W0603,C0103

    data = []
    for route in app.routes:        #pylint:disable=E1101
        data.append([route.name, ', '.join(route.methods), route.path])

    # print header line
    print(f'{"Name":<30} {"Methods":<30} {"Path":<60}')
    print('-'*90)

    # print content lines
    for name, methods, path in data:
        print(f'{name:<30} {methods:<30} {path:<60}')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--port', default=8000,
              help='Listen port for application')
@click.option('--workers', type=click.INT, default=None,
              help='Number of processes for concurrent connections')
@click.option('--loop', default='uvloop',
              help='Event loop type, one of `uvloop`, `asyncio` and `auto`')
@click.option('--log_level', default='error',
              help='Level of logger')
def prod(port, workers, loop, log_level):
    """Run application in production environment
    You can adjust config for webserver by arguments
    """
    run_server(
        port=port,
        workers=workers,
        loop=loop,
        log_level=log_level
    )


@cli.command()
def dev():
    """Run application in development
    In this environment, app working on the process and
    it auto reload when code updated
    """
    run_server(
        host='127.0.0.1',
        workers=1,
        reload=True,
        log_level='debug',
    )


@cli.command()
def routes():
    """List all of routes in application
    """
    show_routes()


if __name__ == '__main__':
    cli()
