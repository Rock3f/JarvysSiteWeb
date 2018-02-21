import json
import requests
from O365 import *
from client.Logger import Logger

logger = Logger('PluginCaller/Mail')


class LastMail(object):

    def __init__(self):
        self.key_words = ["last", "new", "receive"]


    def get_key_words(self):
        return self.key_words

    def execute(self, phrase, user_data):

        token = "Bearer %s" % ("eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFCSGg0a21TX2FLVDVYcmp6eFJBdEh6SjltUlhpQ1B0MDZtMHFNTUhsT1VqUUx6VDFBRjJJZXg0Vk9QdFhuNE15TlcxYTFRdEJnbHQ0UFhWUUNzbG5jUzhPUTRVSjBwMGpBOUdiRGJ5QldYZ3lBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoiU1NRZGhJMWNLdmhRRURTSnhFMmdHWXM0MFEwIiwia2lkIjoiU1NRZGhJMWNLdmhRRURTSnhFMmdHWXM0MFEwIn0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zOGU3MmJiYS0zYzIyLTQzODItOTMyMy1hYzE2MTI5MzEyOTcvIiwiaWF0IjoxNTE5MjIyNzY2LCJuYmYiOjE1MTkyMjI3NjYsImV4cCI6MTUxOTIyNjY2NiwiYWNyIjoiMSIsImFpbyI6IlkyTmdZRkF4REhnODk2VlNkTVpqN2p5TnZuZVAxMjV0NUV5K3pPbC95L1Rtb3BZTzJRc0EiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkpBUlZZUyIsImFwcGlkIjoiMjhiOTg3OWUtMjA2Yy00NmJkLTk3ODYtMmUwM2JjMjJkMDBkIiwiYXBwaWRhY3IiOiIxIiwiZmFtaWx5X25hbWUiOiJHT1NTRVQiLCJnaXZlbl9uYW1lIjoiQW50b2luZSIsImlwYWRkciI6IjgwLjc0LjcyLjE3MyIsIm5hbWUiOiJHT1NTRVQgQW50b2luZSIsIm9pZCI6IjIwNWYzNzI1LTY0N2MtNGIyYS1iMmU1LWE1ZjZmN2ZhNjkzZiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0zMTk4Mzg3NDk1LTE4MTg3OTYxNjEtMzM4MDM5MDQyMi0xNjc3MyIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzN0ZGRTk2REE2MDRFIiwic2NwIjoiRmlsZXMuUmVhZFdyaXRlIE1haWwuUmVhZCBNYWlsLlNlbmQgVXNlci5SZWFkIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiVzBPLXk3MDdOTmJJdTN2VEFBN3JZNG93OGpUUGdqUEpSMGdqeWxTd00yQSIsInRpZCI6IjM4ZTcyYmJhLTNjMjItNDM4Mi05MzIzLWFjMTYxMjkzMTI5NyIsInVuaXF1ZV9uYW1lIjoiYW50b2luZS5nb3NzZXRAeW5vdi5jb20iLCJ1cG4iOiJhbnRvaW5lLmdvc3NldEB5bm92LmNvbSIsInV0aSI6Ik5mLWQyTUdvRUVpNTBFYjk2QzlEQUEiLCJ2ZXIiOiIxLjAifQ.nU78TNiKRcmoazgcRt-uxk4NxfZxjCoarcjvBVAbSFFTcsPZjgChlJrqlqcAq0KefXQKNzVeQcdLoXabVe77bCP1ure78Z6Tz6yndnxo29cD9RWefmz7Nx7YEKiIMaU5slocvVvixvdm07zHOCjS72nNtQSuUkJvAkqF46iYVi20dPbxSqAzWi56sPrldO2RmKT8ElPL-G3Rl_3VKOAAVptmqZoxg-bxR0U-WKycJTLX5FoEUc8l5hGL-AUGrgo7hTcNbQL7kkLQ_vkh_URs7Qv5Ucvh7M97bAUjQEH7tNb0nPeQpxlSIAOtqd9kpNChYwJRY1zPIEsU4p3a5dUsjA")

        r = requests.get("https://graph.microsoft.com/v1.0/me/mailfolders/inbox/messages",
                         headers={"Accept": "application/json", "Authorization": token},
                         params={"$select":"subject,from,receivedDateTime", "$top":"25"})
        mail_data = r.json()

        return {'response': mail_data, 'stored_data': {}}


class SendMail(object):

    def __init__(self):
        self.key_words = ["send"]

    def get_key_words(self):
        return self.key_words

    def execute(self, phrase, user_data):

        splited_phrase = phrase.split('/#/', 3)
        del splited_phrase[0]

        token = "Bearer %s" % ("eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFCSGg0a21TX2FLVDVYcmp6eFJBdEh6TzczX25ORDVxZEMzVlpHbVptbndRR0sza1YxNXpUYmZWdkFWM1JpclBqNGFGMlVTdlZyX3M3OWZvMVpmWnd3MGdvRGw4MFV3N2o2TjQ4b2dGMTRxUmlBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoiU1NRZGhJMWNLdmhRRURTSnhFMmdHWXM0MFEwIiwia2lkIjoiU1NRZGhJMWNLdmhRRURTSnhFMmdHWXM0MFEwIn0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zOGU3MmJiYS0zYzIyLTQzODItOTMyMy1hYzE2MTI5MzEyOTcvIiwiaWF0IjoxNTE5MjI1ODI0LCJuYmYiOjE1MTkyMjU4MjQsImV4cCI6MTUxOTIyOTcyNCwiYWNyIjoiMSIsImFpbyI6IlkyTmdZRGkzbjhzdjdmNEtoM2tCNzM0N2RsMzN2Tml3UmFiTDhjY043U2N5VXVheGUrUUIiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkpBUlZZUyIsImFwcGlkIjoiMjhiOTg3OWUtMjA2Yy00NmJkLTk3ODYtMmUwM2JjMjJkMDBkIiwiYXBwaWRhY3IiOiIxIiwiZmFtaWx5X25hbWUiOiJHT1NTRVQiLCJnaXZlbl9uYW1lIjoiQW50b2luZSIsImlwYWRkciI6IjgwLjc0LjcyLjE3MyIsIm5hbWUiOiJHT1NTRVQgQW50b2luZSIsIm9pZCI6IjIwNWYzNzI1LTY0N2MtNGIyYS1iMmU1LWE1ZjZmN2ZhNjkzZiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0zMTk4Mzg3NDk1LTE4MTg3OTYxNjEtMzM4MDM5MDQyMi0xNjc3MyIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzN0ZGRTk2REE2MDRFIiwic2NwIjoiRmlsZXMuUmVhZFdyaXRlIE1haWwuUmVhZCBNYWlsLlJlYWRXcml0ZSBNYWlsLlNlbmQgVXNlci5SZWFkIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiVzBPLXk3MDdOTmJJdTN2VEFBN3JZNG93OGpUUGdqUEpSMGdqeWxTd00yQSIsInRpZCI6IjM4ZTcyYmJhLTNjMjItNDM4Mi05MzIzLWFjMTYxMjkzMTI5NyIsInVuaXF1ZV9uYW1lIjoiYW50b2luZS5nb3NzZXRAeW5vdi5jb20iLCJ1cG4iOiJhbnRvaW5lLmdvc3NldEB5bm92LmNvbSIsInV0aSI6IkZ0QWZrN05fQTAtY2pQWGlZdTRMQUEiLCJ2ZXIiOiIxLjAifQ.OxEjXbFccDfxt9U9vhh6gUAndpP83d7tK6Ebl4hv9r8UPxl5J7WH5z_yVx-y456b3FPMvPGrduKdn8R1CUuVxdw1l_WMZGDDjGqeRW9OLrNRcO46ELq-weQEgh7rbjCLN3548IT8LojsZ3NMIIreciJvkD1GM9PyvxJHZxiacsa8qlt4660baXH87BE-6ZMtg1_Rr5V6UwanrG1EgAXRNmLrujdlIIdBtcjLmhLQ9rS-z3EX5ORL_mspxdWKUQ2e2sGtU80Az6LjF2V4qDHRcVm-YxOYmMmsmb47koOlRghGaeCrW3FPWsjB_nB8HH6_ofq3lMp-lo8k5mrnwnEVcQ")

        mailToSend = {
            "subject":splited_phrase[1],
            "importance":"Low",
            "body":{
                "contentType":"HTML",
                "content":splited_phrase[2]
            },
            "toRecipients":[
                {
                    "emailAddress":{
                        "address":splited_phrase[0]
                    }
                }
            ]
        }

        r = requests.post("https://graph.microsoft.com/v1.0/me/messages", headers={"Content-type": "application/json", "Authorization": token}, json= mailToSend)
        mail_sended = r.json()

        post_request_send = "https://graph.microsoft.com/v1.0/me/messages/%s/send" % (mail_sended['id'])
        r = requests.post(post_request_send, headers={"Authorization": token})
        print r

        return {'response': r, 'stored_data': {}}


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
