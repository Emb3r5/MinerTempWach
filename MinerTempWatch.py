#!/usr/bin/env python3
import requests
import json
import os
'''
Pre-requisites:
    -Internet Access
    -Openweather API Key (Free version can be throttled)
        Change Zip Code (Use id parameter if outside of US.  See openweathermap for details) and APPID parameters
Note that Temperature and Process name should be modified for specific uses
'''
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=23060,us&APPID=<InstertAPIkey>&units=imperial')
a=(r.json())
mytemp = a["main"]["temp"]
print("The temperature is: " + str(mytemp))

if mytemp > 87.00:
    os.system("pkill ethminer")
