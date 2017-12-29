#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Jack.Xu
#   E-mail  :   xuxiangxiaoup@163.com
#   Date    :   17/12/29 11:11:57
import difflib
text1 = """hello
hello1
hello2
hello3
"""
text1_lines = text1.splitlines()

text2 = """hello
helloa
hellob
hello3c
"""

text2_lines = text2.splitlines()

#显示差异
#d = difflib.Differ()
#diff = d.compare(text1_lines, text2_lines)
#print '\n'.join(list(diff))


#生成美观的HTML展示出来,直接运行结果>diff.html，可以用浏览器打开
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
