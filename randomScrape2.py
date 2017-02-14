from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import URLError
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random
import pprint


pages = []
defaultURL = ""
random.seed(datetime.datetime.now())
# 사이트에서 찾은 외부 URL을 모두 리스트로 수집
allExtLinks = set()
allIntLinks = set()

def getBSObj(url):
    try:
        try:
            html = urlopen(url)
        except URLError as er:
            return None
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
    except AttributeError as e:
        return None

    return bsObj


# 페이지에서 발견된 링크를 모두 리스트로 생성
def getLinks(bsObj, Url, regex):
    links = []
    for link in bsObj.findAll("a", href=re.compile(regex)):
        herfAttr = link.attrs['href']
        if herfAttr is not None:
            if herfAttr not in links:
                links.append(herfAttr)

    return links

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def excludeRegex(Url):
    # 현재 URL을 포함하지 않으며 http나 www로 시작하는 모든 링크 탐색
    excludeRegex = "^(http|www)((?!"+Url+").)*$"
    return excludeRegex

def includeRegex(url):
    # /으로 시작하는 모든 링크 탐색
    includeRegex = "^(/|.*"+url+")"
    return includeRegex

def randomIndex(links):
    if len(links) > 0:
        randomIndex = random.randint(0, len(links) - 1)
        return randomIndex
    else:
        return 0

def getRandomExternalLinks(startingPage):
    bsObj = getBSObj(startingPage)
    if bsObj is not None:
        address = splitAddress(startingPage)[0]
        exRegex = excludeRegex(address)
        externalLinks = getLinks(bsObj, address, exRegex)

        if len(externalLinks) == 0:
            inRegex = includeRegex(address)
            internalLinks = getLinks(bsObj, address, inRegex)
            url = internalLinks[randomIndex(internalLinks)]
            return getRandomExternalLinks(url)
        else:
            return externalLinks[randomIndex(externalLinks)]

def followExternalOnly(startingPage):
    global pages
    global defaultURL
    externalLink = getRandomExternalLinks(defaultURL)
    if externalLink is not None:
        if externalLink not in pages:
            pages.append(externalLink)
        print("Random external link is -> {0}".format(externalLink))
        followExternalOnly(externalLink)
    else:
        print("External link is None!")
        followExternalOnly(pages[randomIndex(pages)])


# defaultURL = "http://oreilly.com"
# followExternalOnly(defaultURL)

def getAllExternalLinks(siteUrl):
    global defaultURL
    bsObj = getBSObj(siteUrl)
    address = splitAddress(defaultURL)[0]

    exRegex = excludeRegex(address)
    externalLinks = getLinks(bsObj, address, exRegex)

    inRegex = includeRegex(address)
    internalLinks = getLinks(bsObj, address, inRegex)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link  in internalLinks:
        if link == "/":
            link = defaultURL
        elif link[0:2] == "//":
            link = "http:" + link
        elif link[0:1] == "/":
            link = defaultURL + link

        if link not in allIntLinks:
            print("About to get link: " + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

try:
    defaultURL = "http://oreilly.com"
    getAllExternalLinks(defaultURL)
except OSError as e:
    print(e)
    pprint(allExtLinks)
    pprint(allIntLinks)
