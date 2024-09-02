#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:46:56 2024

@author: tranthuhuong
"""

N= int(input("Nhập số nguyên dương có hai chữ số: "))
hang_don_vi= N % 10
hang_chuc= N // 10

kq= hang_don_vi + hang_chuc
if 10 <= N <= 99: 
    print("Kết quả là: ", kq)
else:
    print("Không hợp lệ")


