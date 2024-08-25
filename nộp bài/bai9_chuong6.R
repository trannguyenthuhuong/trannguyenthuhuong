#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:31:52 2024

@author: tranthuhuong
"""
import math
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
A = (math.sqrt(a) - math.sqrt(b)) / ((math.pow(a, 1/4)) - (math.pow(b, 1/4)))
B = (math.sqrt(a) + (math.pow(a*b, 1/4))) / ((math.pow(a, 1/4)) + (math.pow(b, 1/4)))

print("Kết quả= ", A - B)




