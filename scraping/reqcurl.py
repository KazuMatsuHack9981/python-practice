import requests as req
import sys

args = sys.argv

if len(args)!=3:
    print("USAGE: python reqcurl.py [url] [filename]")
    sys.exit()

r = req.get(args[1])
filename = args[2]

with open(filename, "wb") as f:
    f.write(r.content)
