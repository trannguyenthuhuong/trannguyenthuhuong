#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:24:27 2024

@author: tranthuhuong
"""
#Bài 17
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)

print("Số nguyên lớn nhất là: ", so_lon_nhat)
print("Số nguyên nhỏ nhất là: ", so_nho_nhat)
