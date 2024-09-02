#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:29:25 2024

@author: tranthuhuong
"""
#Bài 15
import math

a = float(input("Hãy nhập số a: "))
b = float(input("Hãy nhập số b: "))

A =(((a + b) / (math.pow(a, 1/3) + math.pow(b, 1/3))) - (math.pow((a*b), 1/3))) 
B =math.pow(math.pow(a, 1/3) - math.pow(b, 1/3),2)
ket_qua = A / B
print("Kết quả của biểu thức là: ", ket_qua)
