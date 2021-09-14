import requests
from bs4 import BeautifulSoup

load_url = "https://www.google.com/search?q=python+%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89&oq=python++%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89&aqs=chrome..69i57j0i512l2j0i8i30l6.27656j0j15&sourceid=chrome&ie=UTF-8"
# load_url = "http://127.0.0.1:8000/"
# load_url = "https://www.python.jp/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# soup.find(id="appbar")
print(soup.find("nobr"))