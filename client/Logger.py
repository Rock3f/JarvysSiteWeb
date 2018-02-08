#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import os
import errno


def get_time():
    return str(datetime.now())


class Logger(object):
    """ """

    def __init__(self, module, print_it=False, dir_path='/tmp/log/'):
        self.dir_path = dir_path
        self.module = module
        self.print_it = print_it
        self.log_path = dir_path + 'debug.log'
        self.log_error_path = dir_path + 'error.log'
        if not os.path.exists(os.path.dirname(self.log_error_path)):
            try:
                os.makedirs(os.path.dirname(self.log_error_path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    def debug(self, func_name, value):
        self.save_log(self.format_log('Debug', func_name, value))

    def warning(self, func_name, value):
        self.save_log(self.format_log('Warn.', func_name, value))

    def error(self, func_name, value):
        self.save_error_log(self.format_log('Error', func_name, value))

    def format_log(self, mode, func_name, message):
        return "[" + mode + "] " + get_time() + " /" + self.module + "/" + func_name + " : " + str(message)

    def save_log(self, log_message):
        if self.print_it:
            print(log_message)
        with open(self.log_path, 'a+') as f:
            f.write(log_message + '\n')

    def save_error_log(self, log_message):
        self.save_log(log_message)
        with open(self.log_error_path, 'a+') as f:
            f.write(log_message + '\n')


# Logger('Test', './').warning('testFunc','this is the test, pin pin pin pinnnnn')
