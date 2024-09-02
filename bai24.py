#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:04:52 2024

@author: tranthuhuong
"""
#bai24:
gio = int(input("Hãy nhập số giờ: "))
phut = int(input("Hãy nhập số phút: "))
giay = int(input("Hãy nhập số giây: "))

if gio>24 or (phut and giay >60):
    print("Không hợp lệ")
else:
    print("Thời gian hợp lệ")
    