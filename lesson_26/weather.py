import requests
import json
url = 'http://api.openweathermap.org/data/2.5/weather'

my_url = requests.get(url, params={"q": 'Rivne', "units": "metric", 'apiid': '5387623c612af64f83da5b790beef122'},
                      headers={'Content-Type': 'application/json'})
my_url = requests.get(url)
cookes = my_url.cookies
my_url = requests.get(url, cookies=cookes)
#my_url.raise_for_status()
print(my_url.status_code)
print(my_url.headers['content-type'])
print(my_url.json())
