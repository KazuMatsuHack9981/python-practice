import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

url = "https://slackmojis.com/categories/7-party-parrot-emojis"
res = req.get(url)

soup = BeautifulSoup(res.text, "html.parser")

image_urls = soup.select(".downloader")

for i in image_urls:
    print(i.attrs["download"], urljoin(url, i.attrs["href"]))
    r = req.get(urljoin(url, i.attrs["href"]))
    with open("parrots/"+i.attrs["download"], "wb") as f:
        f.write(r.content)
    time.sleep(1)
