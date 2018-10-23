# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:13:04 2018

@author: user
"""
import mod 
a = mod.hello()
print(a)
def mydef(name):
    print('yo' , name)
def mydef2(name):
    print('hi'+ name)
def mydef3(name = 'noname'):
    print('hi', name)
    
def redef(x):
    count = x * 10
    return count

mydef('ho')
mydef2('hola')
mydef(6)
mydef3()
mydef3('lul')

print(redef(5))


class Data:
    def __init__ (self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def person(self):
        print('my name is:',self.name,'and ' +self.sex)
        print('I am '+ str(self.age) +' years old')
p1 = Data('yoto' , 25,'female')
p1.person()        
p1.name = 'idk'
p1.person()

class Employee:
    staff_num = 0
    pay_raise = 1.4
    def __init__(self,name,age,payment):
        
        self.name = name
        self.age = age
        self.payment = payment
        self.email = name+'@gmail.com'
        staff_num +=1
    def info(self):
        print('{} {}'.format(self.name,self.age))
    def pay_up(self):
        self.payment = int(self.payment * Employee.pay_raise)