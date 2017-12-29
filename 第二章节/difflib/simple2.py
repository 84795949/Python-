#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jack.Xu
#   E-mail  :   xuxiangxiaoup@163.com
#   Date    :   17/12/29 11:37:03
import difflib,sys

try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print "Error: "+str(e)
    print "Usage: simple2.py filename1 filename2"
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open (filename,'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print ('Read file Error: '+str(error))
        sys.exit()

if textfile1 == "" or textfile2 == "":
    print "Usage : simple2.py filename1 filename2"
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)

#python simple2.py /home/pcw/test/conf.d/ip.conf /home/pcw/test/conf.d/xss.conf > /home/pcw/test/conf.d/diff.html
