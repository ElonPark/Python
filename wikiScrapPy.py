from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    regex = "^(/wiki/)((?!:).)*$"
    findResult = bsObj.find("div", {"id" : "bodyContent"}).findAll("a", href = re.compile(regex))

    return findResult


links = getLinks("/wiki/kevin_Bacon")
print("links length =  ", len(links))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
