import requests,re
#import urlparse
from bs4 import BeautifulSoup

def webOuter(webUrl):
    #add function:judge 'webUrl' parameter if is not a web url
    #add function:judge 'if the newWebUrl link to webUrl,it may make a Infinite loop',

    webOuterList = set()
    webSoup = BeautifulSoup(requests.get(webUrl).text, "lxml")
    # find 'href' start head 'http' or 'www'
    for newWebUrl in webSoup.findAll('a', href=re.compile("^(http|www).*")):
    # for newWebUrl in webSoup.findAll('a', href=re.compile("^(?!/)+.*")):
        if newWebUrl is not None:
            webOuterList.add(newWebUrl.attrs['href'])

    return webOuterList