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
shop_name = pd.DataFrame(pd.read_csv("./shop.csv",encoding='gbk'))
shop_data = pd.DataFrame(pd.read_csv("./total.csv"))
shop_data['name'] = shop_data['name'].astype('str')
shop_data['app_name'] = shop_data['app_name'].astype('str')
shop_data['s5'] = shop_data['s5'].astype('str')
# for i in range(0,len(shop_name['slsid'])):
for i in range(0,1):
    url = shop_name.iloc[i,3]
    app_url = shop_name.iloc[i,2]
    # dpdata = requests.get(url=url,headers = header).text
    appdata = requests.get(url=app_url).text
    # bsObj = BeautifulSoup(dpdata,'html5lib')
    bsapp = BeautifulSoup(appdata, 'html5lib')
    # shop_data.iloc[i,0] = shop_name.iloc[i,0]
    # shop_data.iloc[i,3]=str(bsObj.title)
    # shop_data.iloc[i,9]=str(bsObj.findAll("dd")[1].em)
    # time.sleep(5)
#shop_data.to_csv("./data310.csv")
print(bsapp.title)
print(bsapp.findAll("span",{"class":"shop-name"}))
print(bsapp.findAll("span",{"class":re.compile("star star-"+"[0-9]+")})[0])
print(bsapp.findAll("span",{"class":"itemNum-val"}))
print(bsapp.findAll("div",{"class":"desc"}).contents)