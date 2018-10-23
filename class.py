# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:04:57 2018

@author: user
"""

a = 3
print (a)
mylist =[1,2,3]
print(mylist)
print(mylist[-1])

a = 0.001
print(type(a))
mylist.append('f')
print(mylist)
print(mylist.index(3))
b = 'my name is wow'
print(b.find('name'))
mylist.remove(3)
print(mylist)
new = '12345123451235'
new2 = new.split('3')
print(new2)
print('3'.join(new2))
print(''.join(new2))
yolo = 'you only see once'
my_dic = {
        'name':yolo,
        'address':'taiwan',
        'phone': '0913235646'
    }
my_dic['what'] = 'anything'
print(my_dic['what'])
print(my_dic)

fruit = 'banana'
if fruit != 'banana':
    print('i want banana')
elif fruit == 'banana':
    print('it ok')

for x in range(1,10,2) :
    print ('x'*x)
y = 0
while y < 5:
    y = y + 1
    print('o'*y)
def callme():
    print('yo')
    
callme()    
    
    









