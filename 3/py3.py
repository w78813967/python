# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:00:47 2018

@author: user
"""

from bs4 import BeautifulSoup
#html_wonder = open ('./py.html','r')
#soup = BeautifulSoup(html_wonder,"html.parser")
#print(soup.prettify())
#
#for link in soup.find_all('a'):
#    print(link.get('href'))
#link = soup.find(id='link')
#print(link)
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>")
#print(sibling_soup.prettify())

b = sibling_soup.b.next_sibling
c = sibling_soup.c.previous_sibling
print(b)
print(c)