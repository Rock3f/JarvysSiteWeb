import json
from O365 import *
from client.Logger import Logger

logger = Logger('PluginCaller/Mail')


class LastMail(object):

    def __init__(self):
        self.key_words = ["last", "new", "receive"]


    def get_key_words(self):
        return self.key_words

    def execute(self, phrase, user_data):

        mail_list = []
        authentification = ('antoine.gosset@ynov.com', 'password')

        try:
            i = Inbox(auth=authentification, getNow=True)
        except ValueError:
            return {'response': 'Wrong password or email', 'stored_data': {}}

        i.getMessages(number=100)
        for m in i.messages:
            subject = m.getSubject()
            sender = m.getSenderName()
            sender_mail = m.getSenderEmail()
            mail = [sender_mail, sender, subject]
            mail_list.append(mail)

        return {'response': mail_list, 'stored_data': {}}


class SendMail(object):

    def __init__(self):
        self.key_words = ["send"]

    def get_key_words(self):
        return self.key_words

    def execute(self, phrase, user_data):

        splited_phrase = phrase.split('/#/', 3)
        del splited_phrase[0]

        authentification = ('antoine.gosset@ynov.com', 'password')
        m = Message(auth=authentification)
        m.setRecipients(splited_phrase[0])
        m.setSubject(splited_phrase[1])
        m.setBody(splited_phrase[2])
        if m.sendMessage():
            json_response = {'data': splited_phrase}
            return {'response': splited_phrase, 'stored_data': {}}
        else:
            json_response = {'data': 'Wrong password or email'}
            return {'response': 'Wrong password or email', 'stored_data': {}}


class Mail(object):
    """"""

    def __init__(self):
        self.key_words = ["mail", "message"]
        self.plugins = [LastMail(), SendMail()]
        self.phrase = ''
        self.name = 'Mail'

    def get_key_words(self):
        return self.key_words

    def execute(self, phrase, user_data):
        self.phrase = phrase
        plugin_found_list = []

        for plugin in self.plugins:
            for key_word in plugin.get_key_words():
                if self.word_correspondence(key_word):
                    plugin_found_list.append(plugin)
                    break

        if len(plugin_found_list) == 1:
            return plugin_found_list[0].execute(phrase, user_data)

        elif len(plugin_found_list) < 1:
            json_response = {'data': 'Wrong password or email'}
            return {'response': json.dumps({'data': 'can t find this function for mail',
                                            'responseStatus': '501'}), 'stored_data': {}}
        else:
            return {'response': json.dumps({'data': 'to much function selected',
                                            'responseStatus': '500'}), 'stored_data': {}}

    def word_correspondence(self, key_word):
        return key_word in self.phrase
