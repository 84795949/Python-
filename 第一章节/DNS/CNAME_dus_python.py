#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jack.Xu
#   E-mail  :   xuxiangxiaoup@163.com
#   Date    :   17/12/28 16:21:21
import dns.resolver
domain = raw_input('Please input an domain: ')
cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()
