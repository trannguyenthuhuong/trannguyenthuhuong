#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:05:06 2024

@author: tranthuhuong
"""

A= float(input("Hãy nhập cân nặng của bạn (kg): "))
B= float(input("Hãy nhập chiều cao của bạn (m): "))

cong_thuc_BMI= A / B**2
print("Số đo kiểm tra sức khoẻ BMI là: ", cong_thuc_BMI)
