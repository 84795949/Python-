#!/usr/bin/python
#coding:utf-8
import IPy
from IPy import IP
ip = IP('192.168.0.0/16')
print ip.len()
for x in ip:
    print x
print ip.len()

a = IP('192.168.1.0/255.255.255.0', make_net=True)
print '根据IP于掩码生成网段格式'
print a

b = IP('192.168.1.0/24').strNormal(3)
print b

