from bs4 import BeautifulSoup
import requests 
import shutil

img_url = 'https://pbs.twimg.com/media/DiZdpp5UwAA0wi8.jpg'
img_name = 'twice'

r = requests.get(img_url, stream=True)
file_name = img_name
print( 'save img to  ./image/'+ file_name + '.jpg')

with open('./image/' + file_name + '.jpg', 'wb+') as out_file:
    shutil.copyfileobj(r.raw, out_file)