from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getBSObj(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
    except AttributeError as e:
        return None

    return bsObj


bsObj = getBSObj("http://pythonscraping.com/pages/warandpeace.html")
if bsObj == None:
    print("bsObj is ", bsObj)
else:
    nameList = bsObj.findAll("span", {"class" : "green"})
    for name in nameList:
        print(name.get_text())

    nameList = bsObj.findAll(text="the prince")
    print("\nthe prince = ", len(nameList))
    allText = bsObj.findAll(id="text")
    print(allText[0].get_text())
