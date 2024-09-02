#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 04:24:15 2024

@author: tranthuhuong
"""

a = int(input("Hãy nhập số nguyên a: "))
b = int(input("Hãy nhập số nguyên b: "))
c = int(input("Hãy nhập số nguyên c: "))

max_value = a
if a < b:
    max_value = b
if a < c:
    max_value = c

print("Giá trị lớn nhất là: ", max_value)
