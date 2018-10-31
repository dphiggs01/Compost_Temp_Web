
from flask import Flask, render_template
from compost_db import CompostDB
from datetime import datetime
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)  # create the application instance :)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
@app.route('/index')
def index():
    compost_db = CompostDB()
    temperature, battery, latest_date_str = compost_db.select_latest_temp_data()
    latest_date = datetime.strptime(latest_date_str, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(latest_date.timetuple()))
    latest_date_str = latest_date.strftime("%m/%d/%Y %I:%M:%S %p")

    ui_data = {'temperature':temperature,'battery_level':battery,'latest_date':latest_date_str,'time_stamp':time_stamp}

    logging.debug("ui_data [{}]".format(ui_data))

    return render_template('index.html', ui_data=ui_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0')
