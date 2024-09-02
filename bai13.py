#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:23:53 2024

@author: tranthuhuong
"""

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
cau_a = f"{day}/{month}/{year}"
cau_b = f"{day}/{month}/{str(year) [2:]}"
cau_c = f"{year}/{month}/{day}"

print("a)", cau_a)
print("b)", cau_b)
print("c)", cau_c)
#ngược lại:
dinh_dang_a= input("Nhập theo định dạng Ngày/Tháng/Năm: ")
dinh_dang_b= input("Nhập theo định dạng Ngày/Tháng/2 số cuối của Năm: ")
dinh_dang_c= input("Nhập theo định dạng Năm/Tháng/Ngày: ")

dda, mma, yyyya = map(int, dinh_dang_a.split("/"))
ddb, mmb, yyyyb = map(int, dinh_dang_b.split("/"))
ddc, mmc, yyyyc = map(int, dinh_dang_c.split("/"))

print("Kết quả định dạng a: ", dda, mma, yyyya)
print("Kết quả định dạng b: ", ddb, mmb, yyyyb)
print("Kết quả định dạng c: ", ddc, mmc, yyyyc)
if yyyyb>50:
    yyyyb = yyyyb +1900
else:
    yyyyb = yyyyb +2000
    





