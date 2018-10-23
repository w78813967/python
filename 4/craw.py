# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:12:50 2018

@author: user
"""

import requests
from bs4 import BeautifulSoup
import shutil

global count 
count = 0
def main_craw(url = 'https://www.ptt.cc/bbs/Hearthstone/index.html'):
     
     r = requests.get(url)
     soup = BeautifulSoup(r.text,"html.parser")
    
     this_page_article_href = get_all_article_href(page_url = url)
     times = len(this_page_article_href)
     for i in range(0,times):
         get_article_content(this_page_article_href[i])
#     get_article_content(this_page_article_href)
#     img_url = 'https://www.ptt.cc'+this_page_article_href
#     print(img_url)
#     title = soup.select('span.article-meta-value')[2].text
#     print('標題：'+title)
     btn = soup.select('div.btn-group > a')    
     up_page_href = btn[3]['href']
     next_page_url = 'https://www.ptt.cc' +up_page_href
     print('change page!')
     main_craw(url = next_page_url)
     
def get_all_article_href(page_url = 'https://www.ptt.cc/bbs/Hearthstone/index.html'):
    article_href = []
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text,"html.parser")
    result = soup.findAll("div",{"class":"title"})
    #print(result)
    for item in result:
        try:
            item_href = item.find("a").attrs["href"]
            article_href.append(item_href)
#            print(item_href)
        except:
            pass  
    #change next page
    return article_href

#count = 0
def get_article_content(this_page_article_href,):
    last_name = []
    count = -1
    url = 'https://www.ptt.cc' + this_page_article_href
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    try:
        title = soup.select('span.article-meta-value')[2].text
        print('標題：'+title)
    except:
        pass
    imgs = soup.find_all('a')
    
    for img in imgs:
        if '.jpg' in img['href'] or '.png' in img['href']:
#            print(img['href'])
            last_name.append(img['href'][21:26])
#            print(last_name)
            count += 1 
#            print(count)
            download_img(img_url = img['href'],img_name = last_name[count])
            
def download_img(img_url,img_name):
    r = requests.get(img_url,stream = True)
    file_name = img_name
    print(img_url,file_name)
    
    try:
        with open(file_name+'.jpg','wb') as out_file:
            shutil.copyfileobj(r.raw,out_file)
    except:
        print('can not save this img')


#    
# 


    
main_craw()
    