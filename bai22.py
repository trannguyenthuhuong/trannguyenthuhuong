#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:47:16 2024

@author: tranthuhuong
"""
#bai22
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

if a==0 and b ==0:
    print("Phuong trình vô số nghiệm")
elif a==0 and b!=0:
    print("pPhương trình vô nghiệm")
else:
    print("Phương trình có nghiệm x= ", -b/a)