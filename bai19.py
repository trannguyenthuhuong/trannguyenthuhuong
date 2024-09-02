#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 04:13:26 2024

@author: tranthuhuong
"""
#bai19

a = int(input("Hãy nhập số nguyên a: "))
b = int(input("Hãy nhập số nguyên b: "))
c = int(input("Hãy nhập số nguyên c: "))
d = int(input("Hãy nhập số nguyên d: "))

min_value = a 

if b < a:
    b = min_value
if c < a:
    c = min_value
if d < a: 
    d = min_value
    
print("Giá trị nhỏ nhất là: ", min_value)

