import traceback
import logging
from urllib.request import Request, urlopen

logger = logging.getLogger()

def temp_from_weather_station():
    ret_val=None
    try:
        req = Request('https://forecast7.com/en/42d37n71d95/rutland/?unit=us', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage_str = webpage.decode("utf-8")
        conditions_pos = webpage_str.find("current-conditions")
        conditions_str = webpage_str[conditions_pos:conditions_pos+100]
        temp_begin_pos = conditions_str.find('temp">')
        temp_end_pos = conditions_str.find('&')
        temp_str = conditions_str[temp_begin_pos+6:temp_end_pos]
        ret_val = int(temp_str)
    except Exception as e:
        logging.error(traceback.format_exc())

    return ret_val

if __name__ == "__main__":
    print(temp_from_weather_station())
