from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import codecs

orgin_url = "http://tests.muwubbq.com/admin/user_info/selectAll_new.php?pageinfo="
total_page = 11
xd_file = codecs.open('E:\巡店系统/table0515.txt','w','utf-8')
i = 1
while i < total_page:
    url = orgin_url + str(i)
    text = requests.get(url).text
    xd_html = BeautifulSoup(text,"html5")
    for n in xd_html.findAll("tr",{"style":"border:1px solid #ACACAC;height:30px;"}):
        shop = n.findAll("td")[0].get_text()
        tb_name = n.findAll("td")[1].get_text()
        score = n.findAll("td")[2].get_text()
        people = n.findAll("td")[3].get_text()
        datetime = n.findAll("td")[4].get_text()
        xd_file.write(shop)
        xd_file.write(",")
        xd_file.write(tb_name)
        xd_file.write(",")
        xd_file.write(score)
        xd_file.write(",")
        xd_file.write(people)
        xd_file.write(",")
        xd_file.write(datetime)
        xd_file.write('\r\n')
    i += 1
    print(url)