from pprint import pprint
import requests
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp =requests.get(url)
a = (resp.json())
for a1 in a:
    if a1['name'] == 'Thanos':
        Thanos = (a1)
        pprint(Thanos)
for a1 in a:
    if a1['name'] == 'Hulk':
        Hulk = (a1)
        pprint(Hulk)

for a1 in a:
    if a1['name'] == 'Captain America':
        Captain_America = (a1)
        pprint(Captain_America)


