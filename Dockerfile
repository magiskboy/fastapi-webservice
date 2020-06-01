FROM python:3.7-alpine AS compile-image

LABEL maintainer="nguyenkhacthanh244@gmail.com" version="1.0"

WORKDIR /app

RUN apk update --no-cache && \
    apk add --no-cache make gcc musl-dev

ADD requirements.txt .

RUN python -mvenv env &&\
    source env/bin/activate &&\
    pip install --no-cache-dir -r requirements.txt

FROM python:3.7-alpine AS runtime-image

WORKDIR /app

COPY --from=compile-image /app/env ./env

ADD . .

EXPOSE 80

ENTRYPOINT ./docker-entrypoint.sh

CMD /bin/sh
