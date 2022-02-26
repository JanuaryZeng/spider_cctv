#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:00:56 2022

@author: zxj
"""

import os
import pandas as pd

data_path = "/home/zxj/dataset/CCTV"

for directory in os.listdir(data_path):
    if directory == '20220201':
        continue
    index = 0
    tmp_path = os.path.join(data_path, directory)
    df = pd.DataFrame(columns=['dir_name','title','label'])
    for dirs in os.listdir(tmp_path):
    
        src = os.path.join(tmp_path, dirs)
        dst = os.path.join(tmp_path, str(index))
        print(src, dst)
        os.rename(src, dst)
        index += 1
        df.loc[index] = [index, dirs, 1]
    df.to_csv(tmp_path+"/label.csv", index = False)
    
    
