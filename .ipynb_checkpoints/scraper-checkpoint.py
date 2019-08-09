#!/usr/bin/env pipenv run python

import requests
from bs4 import BeautifulSoup
import pandas as pd
import string


link = 'http://repository.its.ac.id/view/year/'

r = requests.get(link)
soup = BeautifulSoup(r.content, 'lxml')

tahuns = soup.find_all('li')
kumpulan_tahun = ['http://repository.its.ac.id/view/year/'+tahun.a['href'] for tahun in tahuns if tahun.a['href'].split('.')[0].isdigit()]
print(kumpulan_tahun)

for tahun in kumpulan_tahun: 
    print(f'getting {tahun}')
    req = requests.get(tahun)
    soups = BeautifulSoup(req.content, 'lxml')
    titles = [title.text for title in soups.find_all('em')
              if 'eprints' not in title.text.lower()]
    titles = [title.replace('\r\n','') for title in titles]

    with open('titles.txt','a+') as f: 
        for title in titles: 
            f.writelines(title+'\n')
    print(len(titles))
