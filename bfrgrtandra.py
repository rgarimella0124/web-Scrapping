import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
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
url="https://www.greatandhra.com/movies/reviews/geetha-govindam-review-total-paisa-vasool-91400.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

html = soup.prettify("utf-8")
movie_json = {}

for line in soup.find_all('script',attrs={"type" : "application/ld+json"}):
    details = line.text.strip()
    details = json.loads(details)
    #movie_json["url"] = "https://www.greatandhra.com"+details["url"]
    movie_json["itemReviewed"]={}
    movie_json["itemReviewed"]["name"] = details["itemReviewed"]["name"]
    movie_json["reviewRating"]={}
    movie_json["reviewRating"]["ratingValue"]= details["reviewRating"]["ratingValue"]
    #break

'''with open(movie_json["name"]+".json", 'w') as outfile:
    json.dump(movie_json, outfile, indent=4)
    
with open(‘index.csv’, ‘a’) as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, datetime.now()])'''

with open('data.json', 'w') as outfile:
    json.dump(movie_json[data], outfile)
