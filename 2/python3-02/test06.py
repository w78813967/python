
class Person:
    def __init__(myObject, name, age):
        myObject.name = name
        myObject.age = age

    def myfunc(myObject):
        print("Hello my name is " + myObject.name)
        print("I am " + str(myObject.age) + " years old")

person01 = Person("Henry", 24)
person01.myfunc()
print('------- after change -------')
person01.age = 13
person01.myfunc()
