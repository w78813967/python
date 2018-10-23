import requests
from bs4 import BeautifulSoup

def main_function(url="https://www.ptt.cc/bbs/TWICE/index.html"):
    # first time requests
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    # get next page btn url
    btn = soup.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    # change page   
    next_page_url = 'https://www.ptt.cc' + up_page_href
    print(next_page_url)
    main_function(url=next_page_url)
    
main_function()