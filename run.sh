#!/usr/bin/env bash
NUM_WORKERS=3
TIMEOUT=120
PIDFILE="gunicorn.pid"

if [ -d "/home/ubuntu/Applications/python_envs" ]; then
    source /home/ubuntu/Applications/python_envs/bin/activate
fi

#nohup ./compost_mqtt.py > compost_mqtt.log 2>&1 &
#echo $! > compost_mqtt.pid

#Update the iptable to redirect traffic from port 80 to 8080
#sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080

#To remove the rule find the line number with the command below (A.) and the remove with command (B.) 
#(A.) sudo iptables -L -t nat --line-numbers
#sudo iptables -t nat -D PREROUTING 1
#(B.) sudo iptables -t nat -D <chain> <line_number>

exec gunicorn compost_web:app \
--workers $NUM_WORKERS \
--worker-class gevent \
--timeout $TIMEOUT \
--log-level=debug \
--bind=0.0.0.0:9000 \
--pid=$PIDFILE
