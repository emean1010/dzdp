from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import codecs
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
cm_file = codecs.open('C:/DZDP/comments0403.txt','w','utf-8')

def get_counts(origin_url,star_num = 1, sid = 0, oname = 'a', sname = 'a', ct_num = 37):
    comments = 0
    x = 1
    add_url = "star?pageno="
    while ct_num > 0:
        ct_url = origin_url + "_" + str(star_num) + add_url + str(x)
        comment_text = requests.get(url=ct_url, headers=header).text
        bsComment = BeautifulSoup(comment_text, 'html5lib')
        cm_txt = ""
        for i in range(0, len(bsComment.findAll("li",{"id": re.compile("^rev_[0-9]+$")}))):
            base_data = bsComment.findAll("li", {"id": re.compile("^rev_[0-9]+$")})
            a = base_data[i].findAll("span", {"class": "time"})[0].string
            b = int(str(a[0:2]))
            # 以下依次是星级、口味、环境、服务评分、评论内容
            cm_star = base_data[i].findAll('span',{"class":re.compile("item-rank-rst irr-star[0-9]+")})[0].attrs['class'][1][-2:-1]
            cm_kw = base_data[i].findAll('span',{'class':'rst'})[0].get_text()
            cm_hj = base_data[i].findAll('span', {'class': 'rst'})[1].get_text()
            cm_fw = base_data[i].findAll('span', {'class': 'rst'})[2].get_text()
            pinglun = base_data[i].findAll('div',{"class":"J_brief-cont"})[0]
            try:
                cm_txt = cm_txt.join(pinglun.string)
            except:
                cm_txt = cm_txt.join(pinglun.get_text())
            if b < 13:
                comments += 1
                cm_file.write(str(sls_id.decode('utf-8')))
                cm_file.write("dou@hao")
                cm_file.write(str(origin_name))
                cm_file.write("dou@hao")
                cm_file.write(sls_name)
                cm_file.write("dou@hao")
                cm_file.write(a)
                cm_file.write("dou@hao")
                cm_file.write(str(cm_star))
                cm_file.write("dou@hao")
                cm_file.write(cm_kw)
                cm_file.write("dou@hao")
                cm_file.write(cm_hj)
                cm_file.write("dou@hao")
                cm_file.write(cm_fw)
                cm_file.write("dou@hao")
                try:
                    cm_file.write(cm_txt)
                except:
                    print('评论无法提取'+sname+star2_num+'星'+ct_url)
                    print('sname')
                    # cm_txt = cm_txt.join(str(pinglun.encode('utf-8').decode('utf-8')))
                    # cm_file.write(cm_txt)
                    # print(sls_name+'no pinglun:')
                    # print(cm_txt)
                    # print(pinglun)
                cm_txt = ''
                cm_file.write("huan@hang")
                print(sls_name, star2_num,comments)
            elif b == 16:
                return (comments)
                break
        ct_num -= 20
        x += 1
        time.sleep(4)
        print(sls_name,comments)

for i in range(0,len(shop_name['slsid'])):
    url = shop_name.iloc[i,3]
    dpdata = requests.get(url=url,headers = header,allow_redirects = False).text
    bsObj = BeautifulSoup(dpdata,'html5lib')
    sls_id = str(shop_name.iloc[i,0]).encode('utf-8')
    origin_name = str(shop_name.iloc[i,1]).encode('utf-8').decode('utf-8')
    try:
        sls_name = str(bsObj.title.string[0:-14])
    except:
        print('no name'+origin_name+url)
    # 部分店铺2星或1星数为0，用try避免出错
    try:
        star2_num = str(bsObj.find("a",{"href":re.compile('[a-z0-9\._+]+2star')}).parent.em.string[1:-1])
        get_counts(origin_url=url, star_num=2, sid=sls_id, oname=origin_name, sname=sls_name, ct_num=int(star2_num))
    except:
        print('2star=0')
    try:
        star1_num = str(bsObj.find("a", {"href": re.compile('[a-z0-9\._+]+1star')}).parent.em.string[1:-1])
        get_counts(origin_url=url, star_num = 1, sid = sls_id, oname = origin_name, sname = sls_name, ct_num=int(star1_num))
    except:
        print('1star=0')
    time.sleep(5)