#!/usr/bin/env python2.7
# coding:utf-8
import csv
import json , sys
import requests

csvfile = file('/home/data/ELK/alluser2018-03-29.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    str = json.dumps(line,encoding="UTF-8",ensure_ascii=False)
    list = json.loads(str)
    #print list[0]
    url = 'http://localhost:9200/santak/information/'
    headers = {"Content-type": "application/json"}
    data = {"userid": list[0], "password": list[1], "mail": list[2], "phone": list[3], "username": list[4], "registration_time:": list[5], "ip": list[6]}
    format_data = json.dumps(data)
#    print format_data
    res = requests.post(url, data=format_data, headers=headers, auth=('elastic', 'changeme'))
    print res.text

csvfile.close()
