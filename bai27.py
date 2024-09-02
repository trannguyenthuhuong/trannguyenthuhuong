#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:43:33 2024

@author: tranthuhuong
"""
#bai27
import math
hinh = input("Nhập hình: ")
if hinh == "HV":
    print("Tính S và P của hình vuông")
    a = float(input("Độ dài cạnh: "))
    S = a ** a
    P = a * 4
    print(f"Kết quả: Chu vi hình vuông: {P}, Diện tích hình vuông: {S}")
elif hinh == "HCN":
    print("Tính S và P của hình chữ nhật")
    a = float(input("Nhập chiều dài hình chữ nhật: "))
    b = float(input("Nhập chiều rộng hình chữ nhật: "))
    P = (a+b)*2
    S = a * b
    print(f"Kết quả: Chu vi HCN: {P}, Diện tích HCN: {S}")
elif hinh == "HT":
    print("Tính S và P của hình tròn")
    r = float(input("Bán kính hình tròn: "))
    S = pow(r, 2) * math.pi
    P = 2 * r * math.pi
    print(f"Kết quả: Diện tích: {S}, Chu vi: {P}")
else:
    print("Không hợp lệ.")
