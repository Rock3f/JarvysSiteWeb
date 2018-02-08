import os
import json
import requests
from slackclient import SlackClient


class SendMessage(object):

    def __init__(self):
        self.key_words = ["message", "say", "tell"]

    def get_key_words(self):
        return self.key_words

    def execute(self, phrase):

        try:
            slack_token = ["xoxp-304710346965-305444476326-304531920579-f4b44f3fa623179bfbca734f42beba02"]
            sc = SlackClient(slack_token)

            sc.api_call(
                "chat.postMessage",
                channel="#général",
                as_user = True,
                text="Hello from Python!"
            )
        except ValueError:
            dict = {'Plugin': 'mail', 'responseStatus': '200', 'data': 'Wrong password or email'}
            json_str = json.dumps(dict)
            return json_str

        dict = {'Plugin': 'mail', 'responseStatus': '200', 'data': 'Message send'}
        json_str = json.dumps(dict)
        return json_str


class Slack(object):
    """"""

    def __init__(self):
        self.key_words = ["slack"]
        self.plugins = [SendMessage()]

    def get_key_words(self):
        return self.key_words

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
            return json.dumps({'Plugin': 'Error', 'errorMessage': 'can t find this function for slack', 'responseStatus': '501', 'data': '{}'})
        else:
            return json.dumps({'Plugin': 'Error', 'errorMessage': 'to much slack function selected', 'responseStatus': '500', 'data': '{}'})

    def word_correspondance(self, key_word):
        return key_word in self.phrase
