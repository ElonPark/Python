from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

# try:
#     html = urlopen("http://pythonscraping.com/pages/page1.html")
# except HTTPError as e:
#     print(e)
# else:
#     # print(html.read())
#     bsObj = BeautifulSoup(html.read(), "html.parser")
#
#     # 존재하지 않는 태그에 접근하면 None을 반환
#     print(bsObj.nonExitentTag)
#     # 존재하지 않는 태그에서 다른 태그에 접근하면 AttributedError가 발생
#     # print(bsObj.nonExitentTag.someTag) #AttributeError: 'NoneType' object has no attribute 'someTag'
#     # 이러한 경우 두가지 상황을 명시적으로 체크
#     try:
#         badContent = bsObj.nonExitentTag.anotherTag
#     except AttributeError as e:
#         print("Tag is AttributeError", e)
#     else:
#         if badContent == None:
#             print("badContent Tag is ", badContent)
#         else:
#             print(badContent)
#


# 위 코드를 리팩토링
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title


title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title is ", title)
else:
    print(title)
