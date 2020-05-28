#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import namedtuple
import csv

class Args:

    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c')+1]
        self.d = sys.argv[sys.argv.index('-d')+1]
        self.o = sys.argv[sys.argv.index('-o')+1]

class Config:

    def __init__(self,configfile):
        self.configfile = configfile
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        with open(self.configfile) as f:
            for linef in f:
                linef1 = linef.split('=')
                config[linef1[0].strip()] = float(linef1[1].strip())
        return config

class UserData:

    def __init__(self, userfile):
        self.userfile = userfile
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata = []
        with open(self.userfile) as f:
            userdata = list(csv.reader(f))
        return userdata

'''
class IncomeTexCalculator(object):

    def calc_for_all_userdata(self):
        

    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
        with open() as f:
            writer = csv.writer(f)
            writer.writerows(result)
'''

if __name__ == '__main__':
    a = Config('test.cfg')
    print(a.config)
    b = UserData('user.csv')
    print(b.userdata)
