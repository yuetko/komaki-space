print('第一题：')
# 字符串拼接
str = "QYTANG'day" + ' ' + '2014-9-28'
print(str)

print('''
''')
print('第二题：')
# 通过切片创建子字符串
word = 'scallywag'
sub_word = word[2:-3]
print(sub_word)

print('''
''')
print('第三题：')
# 创造自己的语言，我们将在英语的基础上创建自己的语言：在单词的最后加上-，然后将单词的第一个字母拿出来放到单词的
# 最后，然后在单词的最后加上y，例如，Python，就变成了ython-Py
Lang = 'Python'
New_Lang = Lang[1:] + '-' + Lang[0:2]
print(New_Lang)

print('''
''')
print('第四题：')
# 补齐被删除的代码
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1 name:%-11s' % department1 + 'Manager:%-11s' % depart1_m + 'COURSE FEES:%-11.2f' % COURSE_FEES_SEC\
    + 'The End!'
line2 = 'Department2 name:%-11s' % department2 + 'Manager:%-11s' % depart2_m + 'COURSE FEES:%-11.2f' %COURSE_FEES_Python\
    + 'The End!'
# line1 = 'Department1 name:{0:10} Manager:{1:10} COURSE FEES:{2:<10.2f} The End!'\
#     .format(department1,depart1_m,COURSE_FEES_SEC)
# line2 = 'Department2 name:{0:10} Manager:{1:10} COURSE FEES:{2:<10.2f} The End!'\
#     .format(department2,depart2_m,COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

print('''
''')
print('第五题：')
# RE匹配IP地址，并格式化打印结果
import re
str1 = 'Port-channel1.189   192.168.189.254 YES CONFIG  up'
result = re.match('(\w*-\w*\d\.\d*)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w*\s+\w*\s+(\w*)',str1).groups()
print('-'*100)
print('{0:<8}:{1}'.format('接口',result[0]))
print('{0:<8}:{1}'.format('IP地址',result[1]))
print('{0:<8}:{1}'.format('状态',result[2]))