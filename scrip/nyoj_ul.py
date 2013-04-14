# -*- coding: utf-8 -*- #
import urllib2
import sgmllib
import sys
import string
import nyoj_ul as ul
from pyquery import PyQuery as pq

url = 'http://acm.nyist.net/JudgeOnline/rank.php?page='
##target = open('nyoj_userlist.txt','w')

def userlist_sp(pagenum):
    user_list = ['' for i in range(31)]
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url+str(pagenum), headers = headers)
    try:
        html = urllib2.urlopen(req).read()
    except Exception, e:
        print e
        return [user_list, 0]
    doc = pq(html)
    list_num = len(doc('table#alternate.table-list tr td').find('a'))
    j = 0
    for i in doc('table#alternate.table-list tr td').find('a'):
        table_pq = pq(i)
        table_a = table_pq.text()
        if(table_a != None):
            user_list[j] = table_a
            j = j + 1
    return [user_list,list_num]

def nyoj_userlisr_write():
    for i in range(1000):
        [user_list,list_num] = userlist_sp(i)
        if(list_num == 0):
            break
        target.write(user_list[1].encode('utf8') + '\n')
        target.write('luguozhe' + '\n')




