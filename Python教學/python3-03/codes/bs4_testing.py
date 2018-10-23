
from bs4 import BeautifulSoup
html_alice_wonder = open('./AliceWonderland.html','r')
soup = BeautifulSoup( html_alice_wonder, "html.parser")
# --------------------------------------------------
print("soup.title: ", soup.title)
print("soup.title.string: ", soup.title.string)
print("soup.title.parent: ", soup.title.parent)
print("soup.title.parent.name: ", soup.title.parent.name)
# --------------------------------------------------
print(soup.find('a'))
print(soup.find_all('title', limit=1))
print(soup.find('title'))
# --------------------------------------------------
print(soup.find(id="link3"))
# --------------------------------------------------
head_tag = soup.head
print(head_tag)
head_tag.contents
title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)
# --------------------------------------------------
title_tag = soup.title
print(title_tag)
print(title_tag.parent)
# --------------------------------------------------
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)
# --------------------------------------------------
print(soup.select("body a"))
print(soup.select("html head title"))
