#!/usr/bin/python
#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
import requests
import json
from datetime import date, timedelta
import datetime

def get_weather():
    today = datetime.datetime.now().strftime("%Y%m%d")
    yesterday = (datetime.datetime.today() - timedelta(1)).strftime("%Y%m%d")
    hour = datetime.datetime.today().hour
    input_day = today
    hour_str = ""

    if (hour >= 2 and hour < 5):
        hour_str = "0200"
    elif (hour >= 5 and hour < 8):
        hour_str = "0500"
    elif (hour >= 8 and hour < 11):
        hour_str = "0800"
    elif (hour >= 11 and hour < 14):
        hour_str = "1100"
    elif (hour >= 14 and hour < 17):
        hour_str = "1400"
    elif (hour >= 17 and hour < 20):
        hour_str = "1700"
    elif (hour >= 20 and hour < 23):
        hour_str = "2000"
    elif (hour >= 23):
        hour_str = "2300"
    else: #00:00 ~ 01:59
        input_day = yesterday
        hour_str = "2300"

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
    queryParams = '?' + urlencode(
    { 
        quote_plus('ServiceKey') : 'xDhD67tm+ztLeTKXUd/2gTYy8d+KUCSIR8ejj+vxdhdWdNqEjDEvkxYv1anr1qv16UoabjXKFu9mbebwg/Xvwg==', 
        quote_plus('pageNo') : '1', 
        quote_plus('numOfRows') : '10', 
        quote_plus('dataType') : 'JSON', 
        quote_plus('base_date') : input_day, 
        quote_plus('base_time') : hour_str, 
        quote_plus('nx') : '89', 
        quote_plus('ny') : '91' 
    })

    q_url = url + queryParams
    response = requests.get(q_url)

    w_dict = json.loads(response.text)
    w_response = w_dict.get("response")
    w_body = w_response.get("body")
    w_items = w_body.get("items")
    w_item = w_items.get("item")

    '''
    PTY : Rain or Snow
    SKY : Sunny or Cloudy
    T3H : Temperature for 3 hours
    '''
    weather = []
    for item in w_item:
        if (item.get("category") == "PTY"):
            weather.append(["PTY", item.get("fcstValue")])
        elif (item.get("category") == "SKY"):
            weather.append(["SKY", item.get("fcstValue")])
        elif (item.get("category") == "T3H"):
            weather.append(["T3H", item.get("fcstValue")])

    isRain = False
    isSnow = False
    isSun = False
    isCloud = False
    temperature = weather[2][1]
    #print(weather)

    if (weather[0][1] == "1" or weather[0][1] == "2"): isRain = True
    elif (weather[0][1] == "3" or weather[0][1] == "4"): isSnow = True

    if (weather[1][1] == "1" or weather[1][1] == "2"): isSun = True
    elif (weather[1][1] == "3" or weather [1][1] == "4"): isCloud = True

    if ((not isRain and isCloud) or (not isSnow and isCloud)): return ["cloudy",  int(temperature)]
    elif (isRain): return ["rainy", int(temperature)]
    elif (isSnow): return ["snowy", int(temperature)]
    else: return["sunny", int(temperature)]

if __name__== '__main__':
    print(get_weather())