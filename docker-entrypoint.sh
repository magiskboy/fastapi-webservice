#!/bin/sh

set -e

source env/bin/activate

HOST=0.0.0.0

if [ -z $PORT ]; then
    PORT=80
fi

PHY_CPUS=$(nproc --all)
WEB_CONCURRENCY=$(($PHY_CPUS*2))

LOG_LEVEL=error

LOG_COLOR=--no-use-colors

LOOP=uvloop


echo "\
HOST                : ${HOST}
PORT                : ${PORT}
NUMBER PROCESSES    : ${WEB_CONCURRENCY}
LOOP                : ${LOOP}
LOG LEVEL           : ${LOG_LEVEL}
MEMORY              : $(cat /proc/meminfo | grep MemTotal | sed 's/MemTotal:        //g')"

echo "Server starting..."
uvicorn asgi:app \
    --host ${HOST} \
    --port ${PORT} \
    --workers ${WEB_CONCURRENCY} \
    --loop ${LOOP} \
    --log-level ${LOG_LEVEL} \
    ${LOG_COLOR}
