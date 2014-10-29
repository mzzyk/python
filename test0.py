# -*- coding: utf-8 -*-
## [] 表示list ；（）表示元组或者数组（tuple）；{} 表示集合，字典
data = (2, 3, 5, 9, 12, 5, 54)
## 统计value（=5）的个数
print data.count(5)
a = sorted(data, reverse=False)
print a
for i in a:
    print i,
print '\n'
#集合
b = set("helloL")
c = set([1, 2, 2, 3, 4])
print c
print b

d = {'name': 'zhaoyankang', 'age': 22, 'email': 'zyk921109@126.com'}
print d['email']
print d.items()



