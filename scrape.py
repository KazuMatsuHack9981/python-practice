from bs4 import BeautifulSoup
import urllib.request as req

res = req.urlopen("https://note.nkmk.me/python-list-len/")
soup = BeautifulSoup(res, "html.parser")

linkul = soup.select_one("#related-post > ul")

for li in linkul:
    if li!="\n":
        print(li.find("a"))
