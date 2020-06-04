[![GithubCI](https://github.com/magiskboy/fastapi-webservice/workflows/Test/badge.svg)](https://github.com/magiskboy/fastapi-webservice/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/magiskboy/fastapi-webservice/branch/master/graph/badge.svg)](https://codecov.io/gh/magiskboy/fastapi-webservice)


# fastapi-webservice
Asynchronous webservice


### Dependencies

Project base on [FastAPI](https://fastapi.tiangolo.com/) framework - asynchronous web framework
Using [SQLAlchemy](https://www.sqlalchemy.org/) as ORMs framework


### Install and Start
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn asgi:app --reload --port 5000 --host 127.0.0.1
```
