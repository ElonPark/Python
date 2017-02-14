from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re
# try:
#     import urllib.request as urllib2
# except ImportError:
#     import urllib2


pages = set()

def getBSObj(url):
    try:
        # source = urllib2.urlopen(url).read()
        # html = source.decode("UTF-8")
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
    except AttributeError as e:
        return None

    return bsObj


def getLinks(pageUrl):
    global pages
    url = "https://en.wikipedia.org" + pageUrl
    bsObj = getBSObj(url)
    if bsObj != None:
        for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
            if 'href' in link.attrs:
                newPage = link.attrs['href']
                if newPage not in pages:
                    # 새 페이지 발견
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)


getLinks("")
