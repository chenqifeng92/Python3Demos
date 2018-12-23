import requests
from bs4 import BeautifulSoup

base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
for i in range(1, 14):
    print(base_url.format(i))

    r = requests.get(base_url.format(i))
    b = BeautifulSoup(r.content)
    l = b.find_all('div', {'class': 'content'})
    for s in l:
        print(s.text)
