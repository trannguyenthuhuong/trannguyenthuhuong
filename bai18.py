#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:45:26 2024

@author: tranthuhuong
"""
#bai18:

    
thoi_gian_1 = input("Nhập thời gian thứ nhất (giờ:phút:giây): ")
thoi_gian_2 = input("Nhập thời gian thứ hai (giờ:phút:giây): ")
gio1, phut1, giay1 = map(int, thoi_gian_1.split(":"))
gio2, phut2, giay2 = map(int, thoi_gian_2.split(":"))
tong_giay_1 = gio1 * 3600 + phut1 * 60 + giay1
tong_giay_2 = gio2 * 3600 + phut2 * 60 + giay2

tong = tong_giay_1 + tong_giay_2
hieu = tong_giay_1 - tong_giay_2

gio_tong = tong // 3600
phut_tong = (tong // 3600)%60
giay_tong = tong%60

print(f"Kết quả cộng 2 thời gian: {gio_tong} giờ, {phut_tong} phút, {giay_tong} giây.")

if hieu < 0:
    print("Kết quả không hợp lệ")
else: 
    gio_hieu = hieu//3600
    phut_hieu = (hieu//3600)%60
    giay_hieu = hieu % 60
    print(f"Kết quả trừ 2 thời gian: {gio_hieu} giờ, {phut_hieu} phút, {giay_hieu} giây.")
    
