import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.ptt.cc/bbs/TWICE/index.html")
soup = BeautifulSoup(r.text,"html.parser")

# get next page btn url
btn = soup.select('div.btn-group > a')
up_page_href = btn[3]['href']
print(btn)
print(up_page_href)
# change page   
next_page_url = 'https://www.ptt.cc' + up_page_href
print(next_page_url)
