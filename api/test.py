import requests
# f0a443efaaec4868978a2e693c779496

API_KEY = "f0a443efaaec4868978a2e693c779496"

url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=API_KEY')
response = requests.get(url)
print(response.json())
