print('第一题：')
# 字符串为MAC地址表内容：'166 54a2.74f7.0326 DYNAMIC Gi1/0/11',使用正则表达式匹配

import re
str1 = "'166 54a2.74f7.0326 DYNAMIC Gi1/0/11'"
result = re.match('\'(\w*)\s+(\w*\.\w*\.\w*)\s+(\w*)\s+(\w*.\w*.\w*)\'',str1).groups()
print('{0:<11}:{1}'.format('VLAN ID',result[0]))
print('{0:<11}:{1}'.format('MAC',result[1]))
print('{0:<11}:{1}'.format('Type',result[2]))
print('{0:<11}:{1}'.format('Interface',result[3]))

print('''
''')

print('第二题：')
# 字符串为ASA防火墙show conn（查看连接内容):
# 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
# 使用正则表达式匹配

import re
str2 = "'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'"
result = re.match('.(\w*)\s+\w*\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,5})\s+\w*\s+(\d{1,3}\.\d{1,3}\.\d{1,\
3}\.\d{1,3}.\d{1,5}).\s+\w*\s+(\d{1,2}).(\d{1,2}).(\d{1,2}).\s+\w*\s+(\w*).\s+\w*\s+(\w*).',str2).groups()
print('{0:<20}:{1}'.format('protocol',result[0]))
print('{0:<20}:{1}'.format('server',result[1]))
print('{0:<20}:{1}'.format('localserver',result[2]))
print('{0:<20}:{1:<2}小时{2:>3}分钟{3:>3}秒'.format('idle',result[3],result[4],result[5]))
print('{0:<20}:{1}'.format('bytes',result[6]))
print('{0:<20}:{1}'.format('flags',result[7]))



