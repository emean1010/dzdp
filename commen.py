from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import random
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
shop_name = pd.DataFrame(pd.read_csv("./shop.csv",encoding='utf-8'))
shop_data = pd.DataFrame(pd.read_csv("./total.csv"))

def get_counts(origin_url,star_num = 1, ct_num = 37):
    comments = 0
    x = 1
    add_url = "star?pageno="
    while ct_num > 0:
        ct_url = origin_url + "_" + str(star_num) + add_url + str(x)
        comment_text = requests.get(url=ct_url, headers=header).text
        bsComment = BeautifulSoup(comment_text, 'html5lib')
        for i in range(0, len(bsComment.findAll("li",{"id": re.compile("^rev_[0-9]+$")}))):
            a = bsComment.findAll("li", {"id": re.compile("^rev_[0-9]+$")})[i].findAll("span", {"class": "time"})[
                        0].string
            b = int(str(a[0:2]))
            if b < 16:
                comments += 1
            elif len(a) > 8:
                c = int(str(a[13:15]))
                print("再次评论")
                print(c)
                if c == 17:
                    comments += 1
                else:
                    print("16年更新评论：")
            elif b == 16:
                return (comments)
        ct_num -= 20
        x += 1
        time.sleep(random.randint(4,7))
    return(comments)

for i in range(0,len(shop_name['slsid'])):
    url = shop_name.iloc[i,3]
    app_url = shop_name.iloc[i,2]
    dpdata = requests.get(url=url,headers = header,allow_redirects = False).text
    appdata = requests.get(url=app_url,headers = header).text
    try:
        appdata=appdata.encode('ISO-8859-1').decode()
    except:
        print("正常编码")
        print(app_url)
    bsObj = BeautifulSoup(dpdata,'html5lib')
    bsapp = BeautifulSoup(appdata, 'html5lib')
    shop_data.iloc[i,0] = shop_name.iloc[i,0]
    shop_data.iloc[i,1] = shop_name.iloc[i,1]
    shop_data.iloc[i,2] = bsapp.title.string[0:10]
    shop_data.iloc[i,3] = str(bsObj.title.string[0:-14])
    shop_data.iloc[i,4] = bsapp.find("div",{"class":"brief-info"}).findAll("span")[0].attrs['title']
    shop_data.iloc[i,5] = bsapp.find("div",{"class":"brief-info"}).find("span",{"id":"reviewCount"}).string
    shop_data.iloc[i,6] = bsapp.find("div",{"class":"brief-info"}).find("span",{"id":"comment_score"}).findAll("span")[0].string
    shop_data.iloc[i,7] = bsapp.find("div",{"class":"brief-info"}).find("span",{"id":"comment_score"}).findAll("span")[1].string
    shop_data.iloc[i,8] = bsapp.find("div",{"class":"brief-info"}).find("span",{"id":"comment_score"}).findAll("span")[2].string
    shop_data.iloc[i,9] = str(bsObj.findAll("dd")[1].em.string[1:-1])
    shop_data.iloc[i,10] = str(bsObj.findAll("dd")[2].em.string[1:-1])
    shop_data.iloc[i,11] = str(bsObj.findAll("dd")[3].em.string[1:-1])
    shop_data.iloc[i,12] = str(bsObj.findAll("dd")[4].em.string[1:-1])
    shop_data.iloc[i,13] = str(bsObj.findAll("dd")[5].em.string[1:-1])
    shop_data.iloc[i,14] = get_counts(origin_url=url, star_num=5, ct_num=int(shop_data.iloc[i, 9]))
    shop_data.iloc[i,15] = get_counts(origin_url=url, star_num=4, ct_num=int(shop_data.iloc[i, 10]))
    shop_data.iloc[i,16] = get_counts(origin_url=url, star_num=3, ct_num=int(shop_data.iloc[i, 11]))
    shop_data.iloc[i,17] = get_counts(origin_url=url, star_num=2, ct_num=int(shop_data.iloc[i, 12]))
    shop_data.iloc[i,18] = get_counts(origin_url=url, star_num=1, ct_num=int(shop_data.iloc[i, 13]))
    print(shop_data[i:i+1])
    time.sleep(random.randint(4,7))
    shop_data.to_csv("C:/DZDP/data0715.csv")