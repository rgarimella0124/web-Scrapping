import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
from lxml import html
import requests
import re
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


#For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter url - ' )
url="http://www.cinejosh.com/review/geetha-govindam-review/940"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

html = soup.prettify("utf-8")
movie_json = {}
for line in soup.find_all('script',attrs={"type" : "application/ld+json"}):
    details = line.text.strip()
    details = json.loads(details)
    #movie_json["url"] = "https://www.greatandhra.com"+details["url"]
    #movie_json["itemReviewed"]={}
    #movie_json["itemReviewed"]["name"] = details["itemReviewed"]["name"]
    movie_json["headline"]=details["headline"]
    movie_json["publisher"]={}
    movie_json["publisher"]["name"]=details["publisher"]["name"]
    break
page=requests.get("http://www.cinejosh.com/review/geetha-govindam-review/940")
tree=html.formstring(page.content)

with open('data2.json', 'w') as outfile:
    json.dump(movie_json, outfile)