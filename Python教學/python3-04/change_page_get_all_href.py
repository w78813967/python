import requests
from bs4 import BeautifulSoup

def get_all_articles_href(page_url="https://www.ptt.cc/bbs/TWICE/index.html"):
    article_href =[]
    print('from :', page_url)
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text,"html.parser")
    results = soup.findAll("div",{"class":"title"})
    for item in results:
        try:
            
            item_href = item.find("a").attrs["href"]
            article_href.append(item_href)
            print(item_href)
        except:
            pass
    return article_href

def main_function(url="https://www.ptt.cc/bbs/TWICE/index.html"):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    this_page_article_href = get_all_articles_href(page_url=url)
    btn = soup.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    main_function(url=next_page_url)

main_function()
