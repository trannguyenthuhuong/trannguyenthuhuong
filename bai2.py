#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:43:47 2024

@author: tranthuhuong
"""

a= int(input("Nhập số nguyên a: "))
b= int(input("Nhập số nguyên b: "))

tong= a + b
hieu= a - b
tich= a * b
thuong= a / b
thuong_tron_2_chu_so= round(thuong, 2)
thuong_tron_3_chu_so= round(thuong, 3)

print("Tổng= ", tong)
print("Hiệu= ", hieu)
print("Tích= ", tich)
print("Thương tròn 2 chữ số= ", thuong_tron_2_chu_so)
print("Thương tròn 3 chữ số= ", thuong_tron_3_chu_so)

