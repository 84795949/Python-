#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jack.Xu
#   E-mail  :   xuxiangxiaoup@163.com
#   Date    :   17/12/28 16:33:00

import dns.resolver
import os
import httplib

iplist = []
#appdomain="baidu.com"
appdomain=raw_input('Please input an domain: ')

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/",headers = {"Host": appdomain})

        r = conn.getresponse()
        getcontent = r.read(15)
#        print getcontent

    finally:
        if getcontent=="<html>\n<meta ht":

            print ip," [OK]"
        else:
            print ip+" [Error]"

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error!"
