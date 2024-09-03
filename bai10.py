#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:20:16 2024

@author: tranthuhuong
"""
so_xe = int(input("Nhập số xe gồm 4 chữ số: "))
a = so_xe // 1000
b = (so_xe % 1000)//100
c = ((so_xe % 1000)%100)//10
d = so_xe % 10

so_nut = (a + b + c + d)%10

if (a>9 or a<0) or (b>9 or b<0) or (c>9 or c<0) or (d>9 or d<0):
    print("Số xe không hợp lệ")
else:
    print(f"Số xe của bạn là: {so_nut} nút")
    
    
