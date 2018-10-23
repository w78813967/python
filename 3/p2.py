# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:48:03 2018

@author: user
"""

from PIL import Image
import requests
from io import BytesIO
r = requests.get('https://www.google.com.tw/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
i = Image.open(BytesIO(r.content))
i.save('img.png','png')