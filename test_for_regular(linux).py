# -*-coding:utf-8-*-

print('第一题：')
# 正则表达式练习
import os
import re
ifconfig_result = os.popen('ifconfig ' + 'eno16777728').read()

# 正则表达式查找IP，掩码，广播和mac地址
ipv4_add = re.findall('inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',ifconfig_result)[0]
netmask = re.findall('netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',ifconfig_result)[0]
broadcast = re.findall('broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+',ifconfig_result)[0]
mac_addr = re.findall('ether\s+(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})\s+',ifconfig_result)[0]

# 格式化字符串
format_string = '{0:<10}:{1}'

# 打印结果
print(format_string.format('ipv4_add',ipv4_add))
print(format_string.format('netmask',netmask))
print(format_string.format('broadcast',broadcast))
print(format_string.format('mac_addr',mac_addr))

# 产生网关的IP地址
ipv4_gw = ipv4_add.split('.')
ipv4_gw[3] = '254'
ipv4_gw = '.'.join(ipv4_gw)

# 打印网关的IP地址
print('\n我们假设网关IP地址的最后一位为254，因此网关IP地址为:' + ipv4_gw + '\n')

# Ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall('(ttl|TTL)=',ping_result)
if re_ping_result:
    print ('网关可达！')
else:
    print ('网关不可达！')

print('''
''')

print('第二题：')
# 查看linux网关
import os,re
route_n_result = os.popen('route -n').read()
str = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG',route_n_result)[0]
print ('网关为:' + str)