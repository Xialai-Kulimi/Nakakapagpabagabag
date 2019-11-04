import os
str = '       '
str2 = ''
msg = ''
for i in str.split(' '):
    msg+=i
print(msg)
print(' ')
path = "./data/"
if not os.path.isdir(path):
    os.mkdir(path)
f = open('./data/log', 'w')