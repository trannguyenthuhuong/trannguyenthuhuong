#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:51:35 2024

@author: tranthuhuong
"""

thoi_gian= input("Hãy nhập thời gian (hh:mm:ss): ")
gio, phut, giay= map(int, thoi_gian.split(":"))

tong_giay= gio*3600 + phut*60 + giay
print("Tổng giây là: ", tong_giay)

