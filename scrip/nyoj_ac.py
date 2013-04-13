# -*- coding: utf-8 -*- #
import urllib2
import urllib
import sgmllib
import sys
import string
import nyoj_ul as ul
from pyquery import PyQuery as pq


file_nyojac = open('nyojAC.txt','w')
file_userlist = open('nyojUserList.txt','w')

def nyoj_ac_maxtrix(user_name):
    url = 'http://acm.nyist.net/JudgeOnline/profile.php?userid='
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url + user_name, headers = headers)
    try:
        html = urllib2.urlopen(req).read()
    except Exception, e:
        print e
        return ''
    doc = pq(html)
    len_num = len(doc('table#alternate.table-list tr').eq(1).find('a'))
    ans = user_name +' '+ str(len_num);
    for i in doc('table#alternate.table-list tr').eq(1).find('a'):
        table_a = pq(i).text()
        ans += ' ' + (str)(table_a)
    return ans + '\n'

def nyoj_sp():
    for i in range(500):
        [user_list,list_num] = ul.userlist_sp(i)
        if(list_num == 0):
            break
        for j in range(list_num):
            print (str(i) + ' ' +str(j) + " " + user_list[j])
            ans = nyoj_ac_maxtrix(user_list[j].encode('utf8'))
            file_nyojac.write(ans);
nyoj_sp()

file_nyojac.close()
file_userlist.close()

