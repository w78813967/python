# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:29:08 2018

@author: user
"""

import requests
from bs4 import BeautifulSoup
import shutil

r = requests.get("https://www.ptt.cc/bbs/Hearthstone/M.1532365280.A.049.html")
soup = BeautifulSoup(r.text,"html.parser")
#author = soup.select('span.article-meta-value')[0].text
#board = soup.select('span.article-meta-value')[1].text
title = soup.select('span.article-meta-value')[2].text
#time = soup.select('span.article-meta-value')[3].text
#print('作者:', author)
#print(board,' 看版')
print('標題:', title)
#print('時間:', time)

imgs = soup.find_all('a')
for img in imgs:
    if '.png' in img['href'] or '.jpg' in img['href']:
        img_url = img['href']
        print(img['href'])
        