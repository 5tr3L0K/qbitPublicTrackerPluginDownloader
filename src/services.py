from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import requests as re
import os

req = Request('https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins')
html = urlopen(req)

soup = BeautifulSoup(html, "lxml")

first_table = soup.select_one("table:nth-of-type(1)")

links = []
for link in first_table.findAll('a'):
    if str(link.get('href')[-3:]) == '.py':
        links.append(link.get('href'))

os.mkdir('./OUTPUT')

for i in links:
    r = re.get(str(i), allow_redirects=True)
    preName = str(i).split('/')
    name = preName[-1]
    print('Downloading ... {0}'.format(name))
    open(('./OUTPUT/' + name), 'wb').write(r.content)

print('... done ...')
