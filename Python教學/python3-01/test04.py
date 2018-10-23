myString = 'A,CS1.23.12.32'
print(myString)
new_list = myString.split(',')
print(new_list)
new_list2 = myString.split('.')
print(new_list2)

# join
print(','.join(new_list))
print('.'.join(new_list2))