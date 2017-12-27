#!/usr/bin/python
#coding:utf-8
import psutil
A = psutil
#CPU方面
a = psutil.cpu_times(percpu=True)
print 'CPU详细逻辑信息:\n',a,'\n'
b = psutil.cpu_times().user
print 'CPU用户user的CPU占比时间:\n',b,'\n'
c = psutil.cpu_count()
print 'CPU的逻辑个数:\n',c,'\n'
d = psutil.cpu_count(logical=False)
print 'CPU的物理个数:\n',d,'\n'

#内存方面
e = psutil.virtual_memory()
print '系统内存使用率:\n',e,'\n'

f = psutil.virtual_memory().free
print '系统可用内存:\n',f/1048576,'M\n'

g = psutil.swap_memory()
print '交换空间使用率:\n',g,'\n'

h = psutil.swap_memory().used
print '交换空间可用内存:\n',h/1048576,'M\n'

#磁盘方面
i = A.disk_partitions()
print '磁盘详细信息:\n',i,'\n'

j = A.disk_usage('/')
print '根目录详细信息:\n',j,'\n'

k = A.disk_io_counters()
print '磁盘总IO个数:\n',k,'\n'

l = A.disk_io_counters(perdisk=True)
print '单个分区IO个数，读取信息\n',l,'\n'

#网络信息
m = psutil.net_io_counters()
print '网络信息:\n',m,'\n'

n = psutil.net_io_counters(pernic=True)
print '每个网络借口的IO信息:\n',n,'\n'

#其他信息获取
o = psutil.users()
print '当前用户信息:\n',o,'\n'

import datetime
p = A.boot_time()
p1 = datetime.datetime.fromtimestamp(p).strftime("%y-%m-%d %H:%M:%S")
print '开机时间: ',p1,'\n'


