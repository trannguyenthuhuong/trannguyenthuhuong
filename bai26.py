#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:37:02 2024

@author: tranthuhuong
"""
#bai26a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
temp = 0

if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp

print("Các số theo thứ tự tăng dần là:", a, b, c)
#bai26b:
N = int(input("Nhập số nguyên N: "))
chuoi_so = str (N)
chuoi_sap_xep = ''.join(sorted(chuoi_so)) 
print("Kết quả: ", chuoi_sap_xep)
