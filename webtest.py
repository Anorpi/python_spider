import requests,re
import urlparse
from bs4 import BeautifulSoup

def webInter(webUrl):
    #add function:judge 'webUrl' parameter if is not a web url
    #add function:judge 'if the newWebUrl link to webUrl,it may make a Infinite loop',

    webInterList = set()
    webSoup = BeautifulSoup(requests.get(webUrl).text, "lxml")
    #find 'href' start head '/',at least 2 characters
    for newWebUrl in webSoup.findAll('a', href=re.compile("^/..*")):
        if newWebUrl is not None:
	    webInterList.add(urlparse.urlparse(webUrl).scheme + "://" + urlparse.urlparse(webUrl).netloc + newWebUrl.attrs['href'])

    return webInterList

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
#c=input()
c = 'http://www.google.com'
print c
b=webInter(c)
print "webInter is:"
for x in b:
    print x

a=webOuter(c)
print "webOuter is:"
for y in a:
    print y


