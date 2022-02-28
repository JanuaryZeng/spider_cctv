#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:29:41 2022

@author: zxj
"""

import requests
# from selenium import webdriver
from bs4 import BeautifulSoup
import re
import os
import datetime
import time
time.sleep(60*100)

# driver = webdriver.Firefox(executable_path = "/home/zxj/software/selenium/geckodriver-v0.30.0-linux64/geckodriver")
# driver.implicitly_wait(5)
# driver.get("https://tv.cctv.com/lm/xwlb")

file_path = "/home/zxj/dataset/CCTV"
video_url = "http://dh5.cntv.myalicdn.com/asp/h5e/hls/1200/0303000a/3/default/"
link = "https://tv.cctv.com/lm/xwlb/day/20220221.shtml"

today=datetime.datetime.now()

for i in range(200):
    time_date = today - datetime.timedelta(days=i+1)
    
    time_str = time_date.strftime('%Y%m%d')
    path = os.path.join(file_path, time_str)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        continue
    print(time_str)
    link = "https://tv.cctv.com/lm/xwlb/day/" + time_str + ".shtml"
    html = requests.get(link)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    a_list = soup.find_all("a")

    for i in range(len(a_list)):
        if i == 0 or i == 1 or i % 2 == 0:
        # if not i == 13:
            continue
        title = a_list[i]['alt'][4:].replace(' ','')[0:80]
        video_path = os.path.join(path, title)
        # print(video_path)
        if not os.path.exists(video_path):
            os.mkdir(video_path)
        
        href = a_list[i]['href']
        video_html = requests.get(href)
        video_html.encoding = 'utf-8'
        video_soup = BeautifulSoup(video_html.text, 'lxml')
        #获取新闻文本
        video_text = video_soup.find_all("div",class_='cnt_bd')[0].text
        with open(os.path.join(video_path, "word.txt"), 'wb') as f:
            f.write(bytes(video_text,'UTF-8'))
            f.close()
        
        #获取新闻视频
        output_file = 'video'
        os.chdir(video_path)
        command = 'you-get %s --output-filename %s'%(href,  output_file)
        # print(command)
        os.system(command)
        
    print("========over=======")
        #下载ts文件，但是由于加密原因无法正常演示
        # video_str = video_soup.find_all("div", class_='video')
        # id = re.findall('guid_Ad_VideoCode = \"\w{32}\"', str(video_str))[0][-33:-1]
        # num = 0
        # files = []
        # while True:
        #     video = requests.get(video_url+id+"/"+str(num)+".ts")
        #     if not video.status_code == 200:
        #         break
        #     with open(os.path.join(video_path,str(num)+".ts"),"wb") as f:
        #         f.write(video.content)
        #         f.close()
        #     files.append(str(num)+".ts")
        #     num += 1
        # input_file = '|'.join(files)
        # output_file = 'video.mp4'
        # os.chdir(video_path)
        # command = 'ffmpeg -i "concat:%s" -acodec copy -vcodec copy -absf aac_adtstoasc %s'%	(input_file,output_file)
        # print(command)
        # os.system(command)
        
        #
        # driver.get(href)
        # common = driver.find_element_by_class_name('video_left')
        # time.sleep(5)
        # common = driver.find_element_by_class_name('video')
        # content= common.find_element_by_tag_name('source')
        # html1 = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
        # print(html1)
        # driver.close()
    
        # break
# http://dh5.cntv.myalicdn.com/asp/h5e/hls/1200/0303000a/3/default/fb79eac8f56c4af68ff923d0e56cecb2/0.ts
# http://dh5.cntv.myalicdn.com/asp/h5e/hls/1200/0303000a/3/default/b52e100867774024a7b0390905aa1654/0.ts
