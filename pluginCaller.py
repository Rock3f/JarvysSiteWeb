import requests
import math
import json
import nltk
from textblob import TextBlob
from geotext import GeoText
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')


class Weather(object):
    """ """

    def __init__(self):
        self.key_words = ["weather", "meteo"]

    def get_key_words(self):
        return self.key_words

    def execute(self, phrase):
        print(phrase)

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
        dict = {'Plugin': 'weather', 'Focus': 'Time', 'responseStatus': '200', 'data': data}
        json_str = json.dumps(dict)
        return json_str


class PluginCaller(object) :
    """ """

    def __init__(self):
        self.phrase = "default"
        self.plugins = [Weather()]

    def execute(self, phrase):
        self.phrase = phrase
        finded_plugin = []

        for plugin in self.plugins:
            for key_word in plugin.get_key_words():
                if self.word_correspondance(key_word):
                    finded_plugin.append(plugin)
                    break

        if len(finded_plugin) == 1:
            return finded_plugin[0].execute(phrase)

        elif len(finded_plugin) < 1:
            return json.dumps({'Plugin': 'Error', 'errorMessage': 'can t find plugin', 'responseStatus': '501', 'data': '{}'})
        else:
            return json.dumps({'Plugin': 'Error', 'errorMessage': 'to much plugin selected', 'responseStatus': '500', 'data': '{}'})

    def word_correspondance(self, key_word):
        return key_word in self.phrase

    def print_phrase(self):
        print("print_phrase: ", self.phrase)
