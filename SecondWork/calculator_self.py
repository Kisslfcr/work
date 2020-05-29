#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import namedtuple
import csv


class Args:

    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c') + 1]
        self.d = sys.argv[sys.argv.index('-d') + 1]
        self.o = sys.argv[sys.argv.index('-o') + 1]


class Config:

    def __init__(self, configfile):
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

class IncomeTexCalculator:
    def __init__(self,userdata,config,outfile):
        self._outfile = outfile
        self._userdata = userdata
        self._config = config

    def _calc_for_all_userdata(self):
        result = self._userdata
        for i,j in enumerate(result):
            if int(j[1]) < self._config['JiShuL']:
                result[i].append(self._config['JiShuL']*0.165)
            elif int(j[1]) > self._config['JiShuH']:
                result[i].append(self._config['JiShuL'] * 0.165)
            else:
                result[i].append('{:.2f}'.format(float(j[1]) * 0.165))
        #   计算个税
        for i,j in enumerate(result):
            income = float(j[1])-float(j[2])-5000
            if income < 0:
                result[i].append(0)
            elif income < 1500:
                result[i].append(income*0.03)
            elif income < 4500:
                result[i].append(income*0.1 - 105)
            elif income < 9000:
                result[i].append(income*0.2 - 255)
            elif income < 35000:
                result[i].append(income*0.25 - 1005)
            elif income < 55000:
                result[i].append(income*0.3 - 2775)
            elif income < 80000:
                result[i].append(income*0.35 - 5505)
            else:
                result[i].append(income*0.45 - 13505)
        # 计算实际收入
        for i, j in enumerate(result):
            result[i].append('{:.2f}'.format(float(j[1])-float(j[2])-j[3]))

        return result

    def export(self):
        result = self._calc_for_all_userdata()
        with open(self._outfile ,'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)


if __name__ == '__main__':
    args = Args()
    cfgfile = Config(args.c)
    config = cfgfile.config
    userfile = UserData(args.d)
    userdata = userfile.userdata
    calculatorr = IncomeTexCalculator(userdata,config,'abc.txt')
    calculatorr.export()