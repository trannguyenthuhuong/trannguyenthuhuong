#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:36:03 2024

@author: tranthuhuong
"""

nhap = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
#nhap = nhap.split(", ")
#print(nhap)
nhap = nhap.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "")
sub_string=nhap.split(", ")
for sub in sub_string:
    print(sub)