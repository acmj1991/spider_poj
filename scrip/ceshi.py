# -*- coding: utf-8 -*- #
import urllib2
import sgmllib
import sys
import string
import nyoj_ul as ul
from pyquery import PyQuery as pq
import thread as th

def fun(j, k):
    for i in range(100):
        print i

for i in range(3):
    print '+++++++++++++++' + str(i)
    th.start_new_thread(fun, (12, 10))


