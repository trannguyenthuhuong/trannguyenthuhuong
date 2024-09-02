#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:41:42 2024

@author: tranthuhuong
"""

ki_tu_thuong = input("Hãy nhập 1 kí tự thường: ")
if len(ki_tu_thuong) == 1 and ki_tu_thuong.islower():
    ki_tu_hoa= ki_tu_thuong.upper()
    print("Chữ in hoa của kí tự nhập vào là: ", ki_tu_hoa)
else:
    print("Vui lòng nhập đúng kí tự thường")
    