#!/usr/bin/python
#https://docs.google.com/document/d/1DUYn0wdpSdWkR0oItY3dIrIqd_1P6_KAjJ9sVcuRbbc/edit
code200 = 0
code500 = ''
ip = set()
f = open('nginx.log', 'r')
for line in f.readlines():
    if line != '\n':
        param = line.split(' ')
        if param[8] == '200' and param[5] == '"GET':
            code200 += 1
        elif param[8] == '500':
            code500 += line
        ip.add(param[0])
f.close()

f = open('error500.log', 'w')
f.write(code500)
f.close()

print('Количество успешных get ответов от сервера:', code200)

print('Уникальные IP:', ', '.join(ip))
