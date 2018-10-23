import requests
from bs4 import BeautifulSoup

article_href =[]
r = requests.get("https://www.ptt.cc/bbs/TWICE/index.html")
soup = BeautifulSoup(r.text,"html.parser")
results = soup.findAll("div",{"class":"title"})
print(results)
for item in results:
    item_href = item.find("a").attrs["href"]
    article_href.append(item_href)
    print(item_href)

