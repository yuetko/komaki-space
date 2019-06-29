print('第一题：')
# 把防火墙状态信息表存为字典
import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n" \
           "TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}
for conn in asa_conn.split('\n'):
    re_result = re.match('\w+ \w+ (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) \w+ (\d{1,3}\.'
                         '\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}), idle \d{1,2}:\d{1,2}:\d{1,2}, bytes (\d+), flags\s+(\w+)',\
                         conn).groups()
    asa_dict[re_result[:4]] = (re_result[4:])
print('打印分析后的字典： \n')
print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'

print('\n格式化打印输出\n')
for key,value in asa_dict.items():
    print(f'{src_ip:^10}:{key[0]:^20}|{src:^10}:{key[1]:^20}|{dst_ip:^10}:{key[2]:^20}|{dst:^10}:{key[3]:^20}')
    print(f'{bytes_name:^10}:{value[0]:^20}|{flags:^10}:{value[1]:^20}')
    print(len(f'{src_ip:^10}:{key[0]:^20}|{src:^10}:{key[1]:^20}|{dst_ip:^10}:{key[2]:^20}|{dst:^10}:{key[3]:^20}')*'=')

print('''
''')

print('第二题：')
# 接口排序
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
port_list.sort(key=lambda x:(int(re.findall(r'\d+',x)[0]),int(re.findall(r'\d+',x)[1]),int(re.findall(r'\d+',x)[2]),int(re.findall(r'\d+',x)[3])))
for c in port_list:
    print(c)
