import lxml.html as hp
#from urllib.request import urlopen

#links = hp.parse(urlopen("http://www.python.org")).xpath(".//a[@href]/@href")

import requests

links = hp.fromstring(requests.get("https://www.python.org/").text).xpath(".//a[@href]/@href")
print(links)