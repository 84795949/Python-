#!/usr/bin/python
#coding:utf-8
import psutil
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
print '进程名: ',p.name(),'\n'
print '执行进程的用户名: ',p.username(),'\n'
print '进程占用的CPU信息: ',p.cpu_times(),'\n'
print '输出信息: ',p.communicate(),'\n'
