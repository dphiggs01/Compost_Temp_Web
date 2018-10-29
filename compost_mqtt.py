#!/usr/bin/env python3

from compost_db import CompostDB
import matplotlib.pyplot as plt
import time
import ttn
import json


def plot():
    compost_db = CompostDB()
    dates, temps = compost_db.select_all_temp_data()
    fig = plt.figure(figsize=(20, 5))
    plt.scatter(dates, temps)
    plt.gcf().autofmt_xdate()
    plt.title('Compost Temperatures')
    fig.savefig('./static/images/plot.png')


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
