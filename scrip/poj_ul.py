# -*- coding: utf-8 -*- #
import urllib2
import sgmllib
import sys
import string
import nyoj_ul as ul
from pyquery import PyQuery as pq



def userlist_sp(pagenum, size):
    url1 = 'http://poj.org/userlist?start='
    url2 = '&size='
    url3 = '&of1=solved&od1=desc&of2=submit&od2=asc'
    user_list = ['' for i in range(600)]
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url1+str(pagenum)+url2 + str(size) + url3, headers = headers)
    try:
        html = urllib2.urlopen(req).read()
    except Exception, e:
        print e
        return [user_list, 0]
    doc = pq(html)
    list_num = len(doc('table.a tr')) - 1
    #print list_num
    j = 0
    flag = 0
    for i in doc('table.a tr'):
        table_pq = pq(i)
        table_a = table_pq.text()
        if(table_a != None and flag != 0):
            user_list[j] = table_a.split(' ')[1]
            j = j + 1
        if(flag == 0):
            flag = 1
    return [user_list,list_num]

##print userlist_sp(1)



