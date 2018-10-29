
from flask import Flask, request, session, redirect, url_for, render_template, flash
from compost_db import CompostDB
from datetime import datetime
from dateutil import tz
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py


# Retieve data from 'static' directory. Used most typically for rendering images.
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
@app.route('/index')
def index():
    compost_db = CompostDB()
    temperature, battery, latest_date = compost_db.select_latest_temp_data()
    time_stamp = int(time.mktime(datetime.strptime(latest_date, "%Y-%m-%d %H:%M:%S").timetuple()))
    ui_data = {'temperature':temperature,'battery_level':battery,'latest_date':latest_date,'time_stamp':time_stamp}


    logging.debug("ui_data [{}]".format(ui_data))

    return render_template('index.html', ui_data=ui_data)


# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password',
    WTF_CSRF_ENABLED=True,
))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0')
