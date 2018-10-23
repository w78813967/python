
import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.ptt.cc/bbs/TWICE/M.1532233954.A.02D.html')
soup = BeautifulSoup(r.text,'html.parser')
print(soup.select('span.article-meta-value'))
author = soup.select('span.article-meta-value')[0].text
board = soup.select('span.article-meta-value')[1].text
title = soup.select('span.article-meta-value')[2].text
time = soup.select('span.article-meta-value')[3].text
print('作者:', author)
print(board,' 看版')
print('標題:', title)
print('時間:', time)