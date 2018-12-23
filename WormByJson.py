import requests

r = requests.get('https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0')
print(r.status_code)
j = r.json()
t = j['data']
for i in t:
    print(i['title'], i['casts'])
