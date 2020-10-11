FROM python:3.8-alpine3.12 AS compile-image

LABEL maintainer="nguyenkhacthanh244@gmail.com" version="1.0"

WORKDIR /app

RUN apk update --no-cache && \
    apk add --no-cache make gcc musl-dev

ADD ./requirements.txt .

RUN python -mvenv venv && \
    venv/bin/pip install -r requirements.txt

FROM python:3.8-alpine3.12

WORKDIR /app

COPY --from=compile-image /app/venv ./venv

ADD . .

EXPOSE 8000

ENTRYPOINT PYTHONPATH=. venv/bin/python app prod

CMD /bin/sh
