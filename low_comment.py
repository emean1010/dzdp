from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'_hc.v=f78df6db-3834-a242-d3d2-9cdf9c18cd78.1488961903; __utma=1.160244751.1488962101.1488962101.1488962101.1; __utmz=1.1488962101.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ctu=6a4dd17f4648f8d4405ff252cd7a640128d285c539d6ca69afdbbd909cd40a97; PHOENIX_ID=0a017918-15ab25e3685-2bb69674; lgtoken=334d4707-8c6f-44ae-8f1f-35b595cadb57; dper=3bd3a6a8bea179fda817695935bacfcaf31f68dfbcc23690e86df0a5f953fb71; ll=7fd06e815b796be3df069dec7836c3df; ua=18126161553; JSESSIONID=0719F2F1D62A49D8614E88CA76FF9C52; aburl=1; cy=7; cye=shenzhen; __mta=222713124.1489051228908.1489051228908.1489051228908.1',
    'Host':'www.dianping.com',
    'Referer':'http://www.dianping.com/shop/2230012',
    'pgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

origin_url = "http://www.dianping.com/shop/2230012/review_more"

def get_counts(origin_url,star_num = 5, s5 = 600):
    comments = {}
    x = 1
    add_url = "star?pageno="
    while s5 > 0:
        url = origin_url + "_" + str(star_num) + add_url + str(x)
        comment_text = requests.get(url=url, headers=header).text
        bsComment = BeautifulSoup(comment_text, 'html5lib')
        for i in range(0, len(bsComment.findAll("li",{"id": re.compile("^rev_[0-9]+$")}))):
            a = len(bsComment.findAll("li", {"id": re.compile("^rev_[0-9]+$")})[i].findAll("span", {"class": "time"})[
                        0].string)
            if a == 5:
                comments[i] = a
        s5 = s5 - 20
        x += 1
    return(len(comments))
print(get_counts())