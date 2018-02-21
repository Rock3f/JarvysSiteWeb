#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from client.Logger import Logger
from client.Authentification import Authentification
from client.modules.Mail import Mail
from client.modules.Joke import Joke
from client.modules.Weather import Weather

logger = Logger('PluginCaller', True)
default_auth = Authentification('./../db/db.json', 'ALZq5qSa7V9HOwNyW3nPvOZBKIkce09CLmK9HnelIMA=')


class PluginCaller(object):
    """ """

    def __init__(self, auth_serv=default_auth):
        self.phrase = "default"
        self.plugins = [Weather(), Mail(), Joke()]
        self.auth_service = auth_serv

    def execute(self, phrase, id_user='mail@mail.com'):
        self.phrase = phrase
        plugin_found_list = []

        for plugin in self.plugins:
            for key_word in plugin.key_words:
                if self.word_correspondence(key_word):
                    plugin_found_list.append(plugin)
                    break

        if len(plugin_found_list) == 1:
            plugin = plugin_found_list[0]
            plugin_response = plugin.execute(phrase, self.auth_service.get_user_module_data(id_user, plugin.name))
            self.auth_service.update_user_module_data(id_user, plugin.name, plugin_response['stored_data'])
            return {'Plugin': plugin.name, 'data': plugin_response['response']}

        elif len(plugin_found_list) < 1:
            return json.dumps(
                {'Plugin': 'Error', 'errorMessage': 'can t find plugin', 'responseStatus': '501', 'data': '{}'})
        else:
            return json.dumps(
                {'Plugin': 'Error', 'errorMessage': 'to much plugin selected', 'responseStatus': '500', 'data': '{}'})

    def word_correspondence(self, key_word):
        return key_word in self.phrase

    def print_phrase(self):
        print("print_phrase: ", self.phrase)


# #Phrase test pour weather
# print(PluginCaller().execute("weather in Paris"))
# #Phrase test pour les nouveaux mails
# print(PluginCaller().execute("new mail ?"))
# Phrase test envoie de mail après saisi textuelle
# print(PluginCaller().execute("sendmail/#/antoine.gosset@outlook.fr/#/Test de sujet/#/Test de contenu et de /#/bug"))
# print(PluginCaller().execute("pls a new joke !! :)"))
