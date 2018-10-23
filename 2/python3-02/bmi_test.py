import bmi
input_height_weight = input("input your height and weight and format > 155 40 Apple: ")
my_height_weight = input_height_weight.split(' ')
person1 = bmi.BMITest(int(my_height_weight[0]), int(my_height_weight[1]), my_height_weight[2])
person1.BMI()