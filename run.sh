#!/usr/bin/env bash
NUM_WORKERS=3
TIMEOUT=120
PIDFILE="gunicorn.pid"

if [ -d "/home/ubuntu/Applications/python_envs" ]; then
    source /home/ubuntu/Applications/python_envs/bin/activate
fi

nohup ./compost_mqtt.py > compost_mqtt.log 2>&1 &
echo $! > compost_mqtt.pid


exec gunicorn compost_web:app \
--workers $NUM_WORKERS \
--worker-class gevent \
--timeout $TIMEOUT \
--log-level=debug \
--bind=0.0.0.0:9000 \
--pid=$PIDFILE
