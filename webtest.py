import requests,re
import urlparse
from bs4 import BeautifulSoup

webprobe_domain = 'bilibili.com'
webprobe_soup = BeautifulSoup(requests.get("http://www.bilibili.com/video/game.html").text,"lxml")

external_links=[]
for link in webprobe_soup.find_all("a",href=re.compile("^http.*")):
    if link.attrs['href'] is not None:
         if str(urlparse.urlparse(link.attrs['href']).netloc) != str(webprobe_domain):
            print "********" + str(urlparse.urlparse(link.attrs['href']).netloc) + " domain is:" + webprobe_domain
            if urlparse.urlparse(link.attrs['href']).netloc not in external_links:
                external_links.append(urlparse.urlparse(link.attrs['href']).netloc)

print '####################################'
print external_links[0]
# for i in external_links:
#     print i