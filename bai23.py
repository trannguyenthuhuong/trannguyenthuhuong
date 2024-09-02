#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:36:25 2024

@author: tranthuhuong
"""
#bai23
import math

a = float(input("Hãy nhập số a: "))
b = float(input("Hãy nhập số b: "))
c = float(input("Hãy nhập số a: "))
delta = b**2 - (4*a*c)
if a == 0:
    print("Phương trình có một nghiệm duy nhất x= ", -b/a)
else:
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1x2", (-b/2*a))
    else:
        print("Phương trình có nghiệm phân biệt x1= ", (-b + math.sqrt(delta)) / (2 * a))
        print("Phương trình có nghiệm phân biệt x2= ", (-b + math.sqrt(delta)) / (2 * a))

        