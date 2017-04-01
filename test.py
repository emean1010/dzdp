from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 获取页面所有内链
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href = re.compile("^(/|.*" +includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头切不包含当前URL的链接
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingpage):
    html = urlopen(startingpage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingpage))
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingpage)
        return getExternalLinks(internalLinks[random.randint(0,
                                                             len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("随机外链是: "+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://www.shaoit.com/")