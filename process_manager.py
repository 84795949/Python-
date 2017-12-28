#!/usr/bin/bash
#coding:utf-8

import psutil

a = psutil.pids()
print '列出所有进程PID\n',a,'\n'

b = psutil.Process(2266)
print '详细信息: ',b,'\n'

print '进程名字: ',b.name(),'\n'

print '进程bin路径: ',b.exe(),'\n'

print '进程工作绝对路径: ',b.cwd(),'\n'

print '进程的工作状态: ',b.status(),'\n'

import datetime
print '进程的创建时间: ',datetime.datetime.fromtimestamp(b.create_time()).strftime('%y-%m-%d %H:%M:%S'),'\n'

print '进程UID信息: ',b.uids(),'\n'

print '进程GID信息: ',b.gids(),'\n'

print '进程CPU信息: ',b.cpu_times(),'\n'

print 'get进程CPU亲和度: ',b.cpu_affinity(),'\n'

psutil.Process(2266).cpu_affinity([0,1])

print '参数修改后重新get进程CPU亲和度: ',b.cpu_affinity(),'\n'

psutil.Process(2266).cpu_affinity([0,1,2,3])

print '内存使用率: ',b.memory_percent(),'\n'

print '该进程内存使用详细信息:\n',b.memory_info(),'\n'

print '该进程IO信息: ',b.io_counters(),'\n'

print '打开进程socket的namedutples列表:\n',b.connections(),'\n'

print '进程开启的线程数: ',b.num_threads(),'\n'
