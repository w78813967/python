

def my_second_func():
    print('Call my second function !')

def my_first_func():
    print('Call my first function !')
    my_second_func()

def my_third_func():
    print('Call my third function !')

my_first_func()
my_third_func()
