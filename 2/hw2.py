# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:43:49 2018

@author: user
"""
import hw2mod

h = int(input('請輸入身高：'))
w = int(input('請輸入體重：'))

bm = hw2mod.mybmi(h,w)

print(bm)
        