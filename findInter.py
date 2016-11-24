import requests,re
#import urlparse
from bs4 import BeautifulSoup

def webInter(webUrl):
    #add function:judge 'webUrl' parameter if is not a web url
    #add function:judge 'if the newWebUrl link to webUrl,it may make a Infinite loop',

    webInterList = set()
    webSoup = BeautifulSoup(requests.get(webUrl).text, "lxml")
    for newWebUrl in webSoup.findAll('a', href=re.compile("^/+..*")):
        if newWebUrl is not None:
            webInterList.add(newWebUrl.attrs['href'])

    return webInterList

list = webInter("http://www.v2ex.com/")
for i in list:
    print i



        #print 'hi'
#
# webprobe_domain = 'bilibili.com'
# webprobe_soup = BeautifulSoup(requests.get("http://www.bilibili.com/video/game.html").text,"lxml")
#
# external_links=[]
# for link in webprobe_soup.find_all("a",href=re.compile("^http.*")):
#     if link.attrs['href'] is not None:
#          if str(urlparse.urlparse(link.attrs['href']).netloc) != str(webprobe_domain):
#             print "********" + str(urlparse.urlparse(link.attrs['href']).netloc) + " domain is:" + webprobe_domain
#             if urlparse.urlparse(link.attrs['href']).netloc not in external_links:
#                 external_links.append(urlparse.urlparse(link.attrs['href']).netloc)
#
# print '####################################'
# print external_links[0]
# # for i in external_links:
# #     print i

# def webInter(webUrl):
#     webInterList=set()
#     webSoup = BeautifulSoup(requests.get(webUrl).text, "lxml")
#     for newWebUrl in webSoup.findAll('a',href=re.compile("^/")):
#         print newWebUrl
#         webInterList=webInterList.add(newWebUrl)
#     return  webInterList
#
#
#
#
# a=webInter("http://www.baidu.com")
# for i in a:
#     print i



#print webInterList
# for i in webInterList:
#     print i