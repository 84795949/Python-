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

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print '\n'.join(list(diff))
