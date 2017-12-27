#!/usr/bin/bash
#coding:utf-8

import psutil

a = psutil.pids()
print '列出所有进程PID\n',a,'\n'

b = psutil.Process(8989)
print 'PID8989详细信息: ',b,'\n'

print '8989进程名字: ',b.name(),'\n'

print '8989进程bin路径: ',b.exe(),'\n'

print '8989进程工作绝对路径: ',b.cwd(),'\n'

print '8989进程的工作状态: ',b.status(),'\n'

