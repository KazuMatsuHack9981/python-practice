import urllib.request as req
import sys

args = sys.argv

if not len(args)==3:
    print("uri and filename argument must be given")
    print("usage:\n\tpython wget.py 'https://...' 'test.png'")
    sys.exit()


url      = args[1]
filename = args[2]

req.urlretrieve(url, filename)
