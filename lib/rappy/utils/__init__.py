import os
from datetime import datetime as d


class Log(object):

    def __init__(self, dir_path, prefix=''):
        os.makedirs(dir_path, exist_ok=True)
        today = d.today().strftime('%Y%m%d_%H%S')
        file_path = '{}/log_{}.txt'.format(dir_path, today)
        if prefix:
            file_path = '{}/{}_log_{}.txt'.format(dir_path, prefix, today)
        self.log = open(file_path, 'w')
        self.print_only = False

    def set_print_only(self, print_only):
        self.print_only = print_only

    def info(self, message):
        print(message)
        if not self.print_only:
            self.log.write(str(message) + '\n')

    def close(self):
        self.log.close()
