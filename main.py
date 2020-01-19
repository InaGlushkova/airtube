#!/usr/bin/env python

import urllib.request
import json
import sys

url = 'https://data.sensor.community/airrohr/v1/sensor/6527/'

try:
    json_obj = urllib.request.urlopen(url)

except Exception as e:
    print(e)
    sys.exit()

try:
    data = json.loads(json_obj.read().decode("utf-8"))
    # print(data)

    timestamp = data[1]["timestamp"]
    sensorData = data[1]["sensordatavalues"]

    P1_value = sensorData[0]["value"]
    P2_value = sensorData[1]["value"]

    print('The response is from: \n', timestamp, '\n')
    print('P10  value - ', P1_value, 'mg/m3')
    print('P2.5 value - ', P2_value, 'mg/m3')

except Exception as e:
    print(e)






