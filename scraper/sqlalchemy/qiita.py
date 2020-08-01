import requests as rq
from bs4 import BeautifulSoup as bs4
import urllib.request

# h = {'Authorization': 'Bearer e71402546af8bd8e20443779f52d4486318bbd60'}

url = 'http://youwht.ml/dendou/static/dendou/'
year = '2020'
month = '01'

perfect_url = url+year+month+'_DEN.csv'

req = rq.get(perfect_url)

mem = urllib.request.urlopen(url).read
