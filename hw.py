# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 15:48:25 2018

@author: user
"""
#猜數字 猜錯三次結束
import random

count = 0;
answer = random.randint(0,10)
print(answer) 
print('請輸入答案:')
while count < 3 :
    play = int(input())
    if play == answer:
        print('對')
        count = count + 3
    elif play != answer:
        print('錯')
        count = count + 1
        if count == 3:
            print('沒機會了')

