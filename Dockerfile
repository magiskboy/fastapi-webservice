FROM python:3.7-alpine AS compile-image

LABEL maintainer="nguyenkhacthanh244@gmail.com" version="1.0"

WORKDIR /app

RUN apk update --no-cache && \
    apk add --no-cache make gcc musl-dev

ADD . .

RUN pip install .

EXPOSE 8000

ENTRYPOINT appcli prod

CMD /bin/sh
