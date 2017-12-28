#!/usr/bin/env python
#coding:utf-8

from IPy import IP

ip_s = raw_input('Please input an IP or net-range: ')
ips = IP(ip_s)
if len(ips) > 1:
    print ('网络地址: %s' % ips.net())
    print ('子网掩码: %s' % ips.netmask())
    print ('网络广播地址: %s' % ips.broadcast())
    print ('反向地址解析: %s' % ips.reverseNames()[0])
    print ('子网数: %s' % len(ips))
else:
    print ('IP反向解析: %s' % ips.reverseNames()[0])
    print ('十六进制地址: %s' % ips.strHex())
    print ('二进制地址: %s' % ips.strBin())
    print ('IP地址类型: %s' % ips.iptype())
