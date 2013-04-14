# -*- coding: utf-8 -*- #
import urllib2
import sgmllib
import sys
import string
import poj_ul as ul
from pyquery import PyQuery as pq
import re
import thread as th

##根据用户名获取用户ac题数
def poj_ac_maxtrix(user_name):
    url = 'http://poj.org/userstatus?user_id='
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url + user_name, headers = headers)
    try:
        html = urllib2.urlopen(req).read()
    except Exception, e:
        print e
        return ''
    doc = pq(html)

    doc1 = pq(doc('tr').eq(9))
    doc2 = str(pq(doc1('td').eq(2)).text())
    pa = re.compile(r'\d{4,4}').findall(doc2)
    ans = ''
    j = 0
    for i in pa:
        j += 1
        ans += ' ' + (str)(i)
    ans = user_name + ' ' + str(j) + ans + '\n'
    return ans

##获取用户名 通过用户名查询ac题目
def poj_sp(start, size):
    file_str = '../data/pojAC' + str(start) + '.txt';
    file_pojac = open(file_str,'w+')
    [user_list,list_num] = ul.userlist_sp(start * size, size)
    if(list_num == 0):
        file_pojac.close
        return
    for j in range(list_num):
        print str(start * size) + ' ' +str(j) + ' ' + user_list[j]
        ans = poj_ac_maxtrix(user_list[j].encode('utf8'))
        file_pojac.write(ans)
    file_pojac.close
##开多线程 400 * 100
for i in range(2):
    print '++++++++++++++++++' + str(i)
    th.start_new_thread(poj_sp, (i, 3))
print '----------------end'
##poj_sp(1, 3)
##th.start_new_thread(poj_sp(0, 3))
##th.start_new_thread(poj_sp(1, 3))
##th.start_new_thread(poj_sp(2, 3))
##th.start_new_thread(poj_sp(3, 3))
##file_pojac.close()

