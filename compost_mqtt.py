#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from compost_db import CompostDB
import time
import ttn
import json


def plot():
    print("In Plot")
    compost_db = CompostDB()
    plt.ioff()
    dates, temps = compost_db.select_all_temp_data()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, temps)

    plt.gcf().autofmt_xdate()
    myFmt = mdates.DateFormatter('%y-%m-%d %H:%M:%S')
    plt.gca().xaxis.set_major_formatter(myFmt)

    plt.title('Compost Temperatures')
    fig.savefig('./static/images/plot.svg', bbox_inches='tight')
    #fig.savefig('./static/images/plot.svg')
    plt.close(fig)


def uplink_callback(msg, client):
    print("In call back")
    compost_db = CompostDB()
    # print("msg {}".format(msg))
    # print("msg.payload_fields {}".format(msg.payload_fields))
    celcius_temp = float(msg.payload_fields.temperature)
    farenhiet_temp = round((celcius_temp * 9.0 / 5.0) + 32, 2)
    # print("farenhiet_temp {}".format(farenhiet_temp))
    # print("battery {}".format(msg.payload_fields.battery))
    compost_db.insert_data(farenhiet_temp, msg.payload_fields.battery)
    plot()


def mqtt_get_data():
    print("Starting")
    with open('./config.json') as json_data:
        config = json.load(json_data)
        print(config['app_id'])
        print(config['access_key'])
    handler = ttn.HandlerClient(config['app_id'], config['access_key'])
    # using mqtt client
    mqtt_client = handler.data()
    mqtt_client.set_uplink_callback(uplink_callback)
    mqtt_client.connect()
    while True:
        time.sleep(60)
    # mqtt_client.close()


if __name__ == "__main__":
    mqtt_get_data()
