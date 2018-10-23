# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:53:52 2018

@author: user
"""

import requests

payload = {"q":"python"}
r = requests.get("http://www.google.com/search",params = payload)
f = open(".page.html","w+")
f.write(r.text)