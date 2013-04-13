#coding=utf-8
import urllib2
import sgmllib
import sys
import string
from pyquery import PyQuery as pq

def get(i,e):
    e = pq(e)
    text = e('li a').text()
    print text


url = 'http://acm.nyist.net/JudgeOnline/profile.php?userid=szhhck'
headers = {'Referer':url,}
req = urllib2.Request(url = url, headers = headers)
html = urllib2.urlopen(req).read()
doc = pq(html)
h=doc('table#alternate.table-list').each(get)


#p =pq(url='http://poj.org/userstatus?user_id=dhu_try')
#p('title')
#print p('title').text()