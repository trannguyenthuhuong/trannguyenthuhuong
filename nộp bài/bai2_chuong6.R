#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:50:34 2024

@author: trannguyenthuhuong
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
chia_lay_du = a % b
chia_lay_nguyen = a // b

print("tổng hai số = ", tong)
print("hiệu hai số = ", hieu)
print("tích hai số = ", tich)
print("thương hai số= ", thuong)
print("chia lấy dư = ", chia_lay_du)
print("chia lấy nguyên = ", chia_lay_nguyen)

thuong_tron_2_chu_so = round(thuong, 2)
thuong_tron_3_chu_so = round(thuong, 3)

print("làm tròn hai chữ số= ", thuong_tron_2_chu_so)
print("làm tròn ba chữ số= ", thuong_tron_3_chu_so)
