def number_return_func(x):
    return 5 * x 

def str_return_func(x):
    return 'hello,' + str(x)

print(number_return_func(3))
return_var = number_return_func(3)
print(return_var)
return_str = str_return_func('apple')
print(return_str)
return_str = str_return_func(5)
print(return_str)
