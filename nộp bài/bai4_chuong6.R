#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:58:22 2024

@author: trannguyenthuhuong
"""

gio = int(input(" số giờ: "))
phut = int(input(" số phút: "))
giay = int(input(" số giây: "))
tong_giay = gio * 3600 + phut * 60 + giay 
print("tổng số giây là: ", tong_giay)
if gio>=25:
    print("Giờ không hợp lệ.")
