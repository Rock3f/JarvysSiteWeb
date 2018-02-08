#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import errno
import json
from tinydb import TinyDB, Query
from client.Logger import Logger
from aead import AEAD

query = Query()
logger = Logger('Authentification', True)


def secure_encrypt(password, salt, value):
    return AEAD(salt.encode('utf-8')).encrypt(value.encode('utf-8'), password.encode('utf-8')).decode('utf-8')


def secure_decrypt(password, salt, value):
    return AEAD(salt.encode('utf-8')).decrypt(value.encode('utf-8'), password.encode('utf-8')).decode('utf-8')


class Authentification(object):
    """ This class is the main class to authenticate and store user data """

    def __init__(self, db_file_path='./../db/db.json', salt=AEAD.generate_key().decode('utf-8'), pwd='+1j4@6T3UI7mk1Uqs'
                                                                'dqsdqdsqsd>/M;"tF#Qq@1I"G0$2Vdp+Qd-98"&U,MN&9&4H9_36Vj'):
        if not os.path.exists(os.path.dirname(db_file_path)):
            try:
                os.makedirs(os.path.dirname(db_file_path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        self.db = TinyDB(db_file_path)
        self.db_users = self.db.table('users')
        self.pwd = pwd
        self.salt = salt
        self.auth_secure_encrypt = lambda value: secure_encrypt(self.pwd, self.salt, value)
        self.auth_secure_decrypt = lambda value: secure_decrypt(self.pwd, self.salt, value)
        print(self.salt)
        try:
            self.add_user('mail@mail.com', 'password')
        except ValueError:
            logger.debug('__init__', 'db already init with default user')

    def test_crypt_password(self, crypted_password, password):
        return self.auth_secure_decrypt(crypted_password) == password

    def add_user(self, mail, password):
        db_users = self.db.table('users')
        data = json.dumps({})
        if len(db_users.search(query.mail == mail)) < 1:
            db_users.insert({'mail': mail, 'password': self.auth_secure_encrypt(password), 'data': self.auth_secure_encrypt(data)})
            logger.debug('add_user', 'added user in db : ' + mail)
        else:
            logger.debug('add_user', 'already store user : ' + mail)
            raise ValueError('db_01', 'User already in db')

        # print(db_users.all())

    def remove_user(self, mail, password):
        value = self.db_users.remove((query.mail == mail) & (query.password.test(self.test_crypt_password, password)))
        if len(value) != 1 or value[0] != 1:
            raise ValueError('db_02', 'User not found in db')

    def get_user(self, mail, password):
        db_users = self.db.table('users')
        res = db_users.search((query.mail == mail) & (query.password.test(self.test_crypt_password, password)))
        if len(res) == 1 and secure_decrypt(self.pwd, self.salt, res[0]['password']) == password:
            return res[0]
        else:
            raise ValueError('db_02', 'User not found in db')

    def is_user_in_bd(self, mail, password):
        #TODO : return id (crytp mail)
        try:
            self.get_user(mail, password)
            return True
        except ValueError:
            return False

    def get_user_by_id(self, user_id):
        db_users = self.db.table('users')
        res = db_users.search(query.mail == user_id)
        if len(res) == 1:
            return res[0]
        else:
            raise ValueError('db_02', 'User not found in db')

    # json.loads(auth.auth_secure_decrypt(json.loads(str(auth.get_user("mail@mail.com", "password")).replace('\'', '"'))['data']))
    def string_user_to_json(self, string_user):
        obj_user = json.load(string_user)
        obj_user['data'] = json.loads(self.auth_secure_decrypt(obj_user['data']))
        return obj_user

    def get_user_module_data(self, user_id, module_name):
        user = self.get_user_by_id(user_id)
        user_data = self.auth_secure_decrypt(user['data'])
        json_user_data = json.loads(user_data)
        try:
            return json_user_data[module_name]
        except KeyError:
            logger.debug('get_user_module_data', 'new module : ' + module_name)
            return {}

    def update_user_module_data(self, user_id, module_name, data):
        if len(data) > 0:
            json_user_data = self.get_user_module_data(user_id, module_name)
            json_user_data[module_name] = data
            crypt_user_data = self.auth_secure_encrypt(json.dumps(json_user_data))
            logger.debug('update_user_module_data',
                         self.db_users.upsert({'mail': user_id, 'data': crypt_user_data}, query.mail == user_id))
        else:
            logger.debug('update_user_module_data', 'No change to save')


def tests():
    """ AUTHENTIFICATION TESTS """
    logger.debug('Test', '### START AUTHENTIFICATION TESTS ###')

    # Settings
    import sys
    # salt = AEAD.generate_key().decode('utf-8')
    auth = Authentification('./auth_test_db.json', 'ALZq5qSa7V9HOwNyW3nPvOZBKIkce09CLmK9HnelIMA=')

    # Test 1 : add user
    logger.debug('Test/addUser', '## Test add_user ##')
    try:
        auth.add_user("mail@mail.com", "password")
        logger.debug('Test/addUser', 'Ok')
    except ValueError as error:
        if len(sys.exc_info()[1].args) > 0:
            if sys.exc_info()[1].args[0] == 'db_01':
                logger.error('Test/addUser', sys.exc_info()[1].args[1])

    # Test 2 : is user in bd
    logger.debug('Test/is_user_in_bd', '## Test is_user_in_bd ##')
    if auth.is_user_in_bd("mail@mail.com", "password"):
        logger.debug('Test/is_user_in_bd', 'Ok')
    else:
        logger.debug('Test/is_user_in_bd', 'KO : user should be in bd')

    # Test 3 : get user
    logger.debug('Test/getUser', '## Test get_user ##')
    user = auth.get_user("mail@mail.com", "password")
    logger.debug('Test/getUser', 'Ok :')
    logger.debug('Test/getUser', user)

    # Test 4 : get user by id
    logger.debug('Test/getUserById', '## Test get_user ##')
    user = auth.get_user_by_id("mail@mail.com")
    logger.debug('Test/getUserById', 'Ok :')
    logger.debug('Test/getUserById', user)

    # Test 5 : decrypt user password
    logger.debug('Test/decryptUserPassword', '## Test auth_secure_decrypt ##')
    obj_user = json.loads(str(user).replace('\'', '"'))
    decrypt_password = auth.auth_secure_decrypt(obj_user['password'])
    logger.debug('Test/decryptUserPassword', 'Ok :')
    logger.debug('Test/decryptUserPassword', decrypt_password)

    # Test 6 : decrypt user data
    logger.debug('Test/decryptUserData', '## Test auth_secure_decrypt ##')
    decrypt_data = auth.auth_secure_decrypt(obj_user['data'])
    logger.debug('Test/decryptUserData', 'Ok :')
    logger.debug('Test/decryptUserData', decrypt_data)

    # Test 7 : update user module data
    logger.debug('Test/update_user_module_data', '## Test update_user_module_data ##')
    str_json_data = json.dumps({'nb_tets_run': 10})
    auth.update_user_module_data('mail@mail.com', 'Test', str_json_data)
    user = auth.get_user_by_id("mail@mail.com")
    obj_user = json.loads(str(user).replace('\'', '"'))
    user_data = auth.auth_secure_decrypt(obj_user['data'])
    json_data = json.loads(user_data)
    if json_data['Test'] == str_json_data:
        logger.debug('Test/update_user_module_data', 'Ok :')
    else:
        logger.debug('Test/update_user_module_data', 'KO :')
    logger.debug('Test/update_user_module_data', json.dumps(json_data))

    # Test 8 : remove user
    logger.debug('Test/remove_user', '## Test remove_user (with user) ##')
    try:
        auth.remove_user("mail@mail.com", "password")
        logger.debug('Test/remove_user', 'Ok')
    except ValueError as error:
        logger.error('Test/remove_user', 'KO : [' + sys.exc_info()[1].args[0] + ']' + sys.exc_info()[1].args[1])

    # Test 9 : remove user
    logger.debug('Test/remove_user', '## Test remove_user (without user) ##')
    try:
        auth.remove_user("mail@mail.com", "password")
        logger.error('Test/remove_user', 'KO : should return a error')
    except ValueError as error:
        logger.debug('Test/remove_user', 'Ok : [' + sys.exc_info()[1].args[0] + ']' + sys.exc_info()[1].args[1])

    logger.debug('Test', '### END AUTHENTIFICATION TESTS ###')


# tests()
