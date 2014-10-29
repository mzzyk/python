#-*-coding:utf-8 -*-
__author__ = 'ZYK'
##class简单应用
class person(object):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__count = 1
        person.count += 1


p1 = person('yank', 22)
print('The count of person id:', p1.count)
p2 = person('zhao', 20)
print p2.age
print('The count of person id:', p2.count)
p3 = person('kang', 23)
print p2.count
