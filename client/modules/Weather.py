#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from client.geotext.geotext import GeoText


class Weather(object):
    """ """

    def __init__(self):
        self.key_words = ["weather", "meteo"]
        self.name = 'Weather'

    def execute(self, phrase, user_data):

        """blob = TextBlob(phrase)
        print(blob.correct())
        print (blob.tags)
        city = blob.noun_phrases
        print(city)"""

        places = GeoText(phrase)
        city = places.cities

        if not city:
            print('none')
            city = ["Nantes"]

        r = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=%s,fr&appid=5de86d565abd26818fde3e7d16b4c358" % city[0])
        data = r.json()
        dict = {'Focus': 'Time', 'data': data}
        json_str = json.dumps(dict)
        return {'responseStatus': '200', 'response': json_str, 'stored_data': {}}
