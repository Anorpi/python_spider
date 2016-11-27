import requests,re
import urlparse
from bs4 import BeautifulSoup

def webInter(webUrl):
    #add function:judge 'webUrl' parameter if is not a web url
    #add function:judge 'if the newWebUrl link to webUrl,it may make a Infinite loop',

    webInterList = set()
    webSoup = BeautifulSoup(requests.get(webUrl).text, "lxml")
    #find 'href' start head '/',at least 2 characters
    for newWebUrl in webSoup.findAll('a', href=re.compile("^/(?!/)..*")):
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
webUrl = 'http://www.google.com/advanced_search?hl=en&authuser=0'
print "webUrl is:" + webUrl
for x in webInter(webUrl):
    print "x is:" + x
   # for xx in webInter(x):
   #     print "xx is:" + xx
    

#a=webOuter(c)
#print "webOuter is:"
#for y in a:
#    print y
#
#
