#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:24:19 2024

@author: tranthuhuong
"""
#bai25:


chu_cai = input("Nhập một chữ cái: ")
chu_hoa = chu_cai.upper()
chu_thuong = chu_cai.lower()
if chu_hoa != chu_cai:
    print("Chữ thường tương ứng là: ", chu_hoa)
else:
    print("Chữ hoa tương ứng là: ", chu_thuong)