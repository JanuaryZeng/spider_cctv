#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:30:48 2022

@author: zxj
"""

import os
import pandas as pd

data_path = "/home/zxj/dataset/CCTV"

for directory in os.listdir(data_path):
    tmp_path = os.path.join(data_path, directory)
    csv_path = os.path.join(tmp_path, "label.csv")
    df = pd.read_csv(csv_path)
    df['images'] = 0
    # df['dir_name'] -= 1
    print(tmp_path)
    for dirs in os.listdir(tmp_path):
        if dirs == "label.csv":
            continue
        path = os.path.join(tmp_path, dirs+"/images")
        if os.path.exists(path):
            df.loc[int(dirs),'images'] = 1
        
    df.to_csv(csv_path, index=False)
        


