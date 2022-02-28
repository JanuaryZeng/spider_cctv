#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:00:56 2022

@author: zxj
"""
# 用于将中文文件夹名称修改为0-100的数字
import os
import pandas as pd

data_path = "/home/zxj/dataset/CCTV"

for directory in os.listdir(data_path):
    index = 0
    tmp_path = os.path.join(data_path, directory)
    df = pd.DataFrame(columns=['dir_name','title','label'])
    if os.path.exists(os.path.join(tmp_path,"label.csv")):
        continue
    for dirs in os.listdir(tmp_path):
    
        src = os.path.join(tmp_path, dirs)
        dst = os.path.join(tmp_path, str(index))
        print(src, dst)
        os.rename(src, dst)
        df.loc[index] = [index, dirs, 1]
        index += 1
    df.to_csv(tmp_path+"/label.csv", index = False)
    
    
