# # -*- coding:utf-8 -*-
import requests,base64,re
import lxml.html as lh
from contextlib import closing
url = "http://qixin8.map456.com/vin2017091411.aspx"
headers = {
       "Host":"qixin8.map456.com",
       "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
       "Accept-Encoding": "gzip, deflate",
       "Accept-Language": "zh-cn",
       "Content-Type": "application/x-www-form-urlencoded",
       "Origin": "http://qixin8.map456.com",
       "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1",
       "Referer":"http://qixin8.map456.com/vin2017091411.aspx",
       "Upgrade-Insecure-Requests":'1',
}
# 爬post参数
# with closing(requests.get(url,headers=headers)) as req:
#        content = lh.fromstring(req.text)
#        __VIEWSTATE = content.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
#        __VIEWSTATEGENERATOR = content.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
#        __EVENTVALIDATION = content.xpath('//input[@id="__EVENTVALIDATION"]/@value')[0]
# print __VIEWSTATE
# print __VIEWSTATEGENERATOR
# print __EVENTVALIDATION
__VIEWSTATE = '/wEPDwULLTExMzAwMTYyOTFkZNOeRBVNb8Ih78dR+O/KrrY0lNOKKOiZ1XErZWCbaXc7'
__VIEWSTATEGENERATOR = '090766F8'
__EVENTVALIDATION = '/wEdAAO4RCXJ6HRrwzKaTpmai0gtfe7nBIAqlvrTIa1Kh8yyul/dZjW/tHAJcLmf/EpfSVyTe5xK6SnmNZmwITWWkPX0ckBhWWPyj/NMwqDV3MB+OQ=='
txt_key = 'LSYYDACKXG1111111'
btn_search = '查询'.decode('utf-8').encode('gbk','ignore')
# print btn_search
post_data = {
       "__VIEWSTATE" : __VIEWSTATE,
       "__VIEWSTATEGENERATOR":__VIEWSTATEGENERATOR,
       "__EVENTVALIDATION":__EVENTVALIDATION,
       "txt_key":txt_key,
       "btn_search":btn_search
}

with closing(requests.post(url,headers=headers,data=post_data)) as req_post:
       content_post = lh.fromstring(req_post.text)
       info = content_post.xpath('//input[@id="__VIEWSTATE"]/@value')

if info:
       #print info[0]
       # base64解码
       info = base64.b64decode(info[0])
       # 正则匹配去掉多余的内容
       info = re.findall(r'<.*>',info)[0]
       pattern = re.compile('<tr><td align="center"><span class="t1">(.*?)</span></td><td align="right"><span class="t1">(.*?)</span></td></tr>')
       info = pattern.findall(info,0)
       with open('output', 'w') as f :
              for i in xrange(2,24):
                     f.writelines('%s%s\n' % (info[i][0],info[i][1]))
                     print info[i][0].decode("utf-8") + info[i][1].decode("utf-8")
# print info[0][0].decode('utf-8')