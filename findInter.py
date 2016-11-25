import requests,re
#import urlparse
from bs4 import BeautifulSoup

def webInter(webUrl):
    #add function:judge 'webUrl' parameter if is not a web url
    #add function:judge 'if the newWebUrl link to webUrl,it may make a Infinite loop',

    webInterList = set()
    webSoup = BeautifulSoup(requests.get(webUrl).text, "lxml")
    #find 'href' start head '/',at least 2 characters
    for newWebUrl in webSoup.findAll('a', href=re.compile("^/..*")):
        if newWebUrl is not None:
            webInterList.add(newWebUrl.attrs['href'])

    return webInterList

