import re
import os

f = open('corton-stat.sql', 'r')
data = f.read()
f.close()

lis = re.split('INSERT INTO ', data)

h = 0

for elem in lis:        
    h = h + 1  
    ff = 'sql/' + str(h) + '.sql'
    f = open(ff, 'w')
    if h == 1:
        f.write(elem)
    else:
        f.write('INSERT INTO ' + elem)
    f.close()
    ff = "mysql --defaults-extra-file=/home/dmitriy/Рабочий\ стол/corton/.my.cnf -h 192.168.43.4 -u corton corton-stat < " + ff
    os.system(ff)
    print (h)
