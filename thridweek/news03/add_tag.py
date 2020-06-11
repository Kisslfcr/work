#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.shiyanlou
f1 = {'tag':['te
