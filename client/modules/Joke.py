#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from client.Logger import Logger

logger = Logger('PluginCaller/Joke', True)


class Joke(object):
    """ """

    def __init__(self):
        self.key_words = ["joke", "blague"]
        self.name = 'Joke'

    def execute(self, phrase, user_data):
        logger.debug('execute', user_data)
        json_joke = self.get_joke('eg')
        if len(user_data) == 0:
            user_data = {'already_display_joke': []}
        elif len(user_data['already_display_joke']) > 20:
            user_data['already_display_joke'] = user_data['already_display_joke'].reverse().pop().reverse()

        already_display_joke = user_data['already_display_joke']
        if json_joke['id'] in already_display_joke:
            while json_joke['id'] not in already_display_joke:
                json_joke = self.get_joke('eg')

        already_display_joke.append(json_joke['id'])

        user_data['already_display_joke'] = already_display_joke
        logger.debug('execute', user_data)
        return {'responseStatus': json_joke['status'], 'response': json_joke, 'stored_data': user_data}

    def get_joke(self, language='eg'):
        if language == 'eg':
            headers = {'Accept': 'application/json'}
            r = requests.get('http://icanhazdadjoke.com/', headers=headers)
            return r.json()
        else:
            return {'id': 'TvPfV8prOuc', 'joke':'Quelle est la femme du hamster ?\r\n\r\nL\'Amsterdam', 'status': 200}
