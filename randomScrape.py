from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random

# pages = set()
pages = []
random.seed(datetime.datetime.now())

#Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,
                                  len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def randomIndex(links):
    if len(links) > 0:
        randomIndex = random.randint(0, len(links) - 1)
        return randomIndex
    else:
        return 0

def followExternalOnly(startingSite):
    global pages
    externalLink = getRandomExternalLink("http://oreilly.com")
    if externalLink is not None:
        if externalLink not in pages:
            pages.append(externalLink)
        print("Random external link is -> {0}".format(externalLink))
        followExternalOnly(externalLink)
    else:
        print("External link is None!")
        followExternalOnly(pages[randomIndex(pages)])

followExternalOnly("http://oreilly.com")

if len(pages) >= 1000:
    print("all save link")
    for i in pages:
        print(i)


# //////////////////////////////////////////////////

# def getBSObj(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#
#     try:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#     except AttributeError as e:
#         return None
#
#     return bsObj
#
#
# # 페이지에서 발견된 링크를 모두 리스트로 생성
# def getLinks(bsObj, Url, regex):
#     links = []
#     for link in bsObj.findAll("a", href=re.compile(regex)):
#         herfAttr = link.attrs['href']
#         if herfAttr is not None:
#             if herfAttr not in links:
#                 links.append(herfAttr)
#
#     return links
#
# def splitAddress(address):
#     addressParts = address.replace("http://", "").split("/")
#     return addressParts
#
# def excludeRegex(Url):
#     # 현재 URL을 포함하지 않으며 http나 www로 시작하는 모든 링크 탐색
#     excludeRegex = "^(http|www)((?!"+Url+").)*$"
#     return excludeRegex
#
# def includeRegex(url):
#     # /으로 시작하는 모든 링크 탐색
#     includeRegex = "^(/|.*"+url+")"
#     return includeRegex
#
# def randomIndex(links):
#     if len(links) > 0:
#         randomIndex = random.randint(0, len(links) - 1)
#         return randomIndex
#     else:
#         return 0
#
# def getRandomExternalLinks(startingPage):
#     bsObj = getBSObj(startingPage)
#     if bsObj is not None:
#         address = splitAddress(startingPage)[0]
#         exRegex = excludeRegex(address)
#         externalLinks = getLinks(bsObj, address, exRegex)
#
#         if len(externalLinks) == 0:
#             inRegex = includeRegex(startingPage)
#             internalLinks = getLinks(bsObj, address, inRegex)
#             if len(internalLinks) > 0:
#                 url = internalLinks[random.randint(0, len(internalLinks)-1)]
#                 return getRandomExternalLinks(url)
#         else:
#             return externalLinks[random.randint(0, len(externalLinks)-1)]
#
# def followExternalOnly(startingPage):
#     global pages
#     externalLink = getRandomExternalLinks(startingPage)
#     if externalLink is not None:
#         if externalLink not in pages:
#             pages.append(externalLink)
#         print("Random external link is -> {0}".format(externalLink))
#         followExternalOnly(externalLink)
#     else:
#         print("External link is None!")
#         followExternalOnly(pages[randomIndex(pages)])
#
#
# followExternalOnly("http://oreilly.com")
