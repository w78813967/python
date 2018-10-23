
import requests
from bs4 import BeautifulSoup

def get_articles_content(this_page_article_href="/bbs/TWICE/M.1532091026.A.BAF.html"):
    image_count = 0
    r = requests.get("https://www.ptt.cc" + this_page_article_href )
    soup = BeautifulSoup(r.text,"html.parser")
    try:
        author = soup.select('span.article-meta-value')[0].text
        board = soup.select('span.article-meta-value')[1].text
        title = soup.select('span.article-meta-value')[2].text
        time = soup.select('span.article-meta-value')[3].text
        print('作者:', author)
        print(board,' 看版')
        print('標題:', title)
        print('時間:', time)
    except:
        pass
    imgs = soup.findAll('a')
    for img in imgs:
        if '.jpg' in img['href']:
            print(img['href'])
            image_count += 1

get_articles_content()