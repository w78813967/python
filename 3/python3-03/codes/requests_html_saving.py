import requests
payload = {"q":"python"}
r = requests.get("http://www.google.com/search", params=payload)
f = open("./page.html","w+")
f.write(r.text)
