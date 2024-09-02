#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 03:39:01 2024

@author: tranthuhuong
"""

hh = int(input("Nhập số giờ (h): "))
mm = int(input("Nhập số phút (p)): "))
ss = int(input("Nhập số giây (s)): "))
tong_so_giay= (hh * 3600) + (mm * 60) + ss

print(f"{hh} giờ {mm} phút {ss} giây tương đương với {tong_so_giay} giây")