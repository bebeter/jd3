#!/usr/bin/env python
#-*- coding: utf-8 -*-


import socket
from pyquery import PyQuery as pq
from lxml import etree
import urllib2
import re
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def getLine (fn):
   items=[]
   f=open(fn)
   for line in f.readlines():
      #print line;count
      #if   data.count(line)==0:
      items.append(line.strip())

   f.close()
   return items


fn=r"F:\ts\jd2\brand.txt"

brands = getLine(fn)
for brand in brands:
    print  "insert into `ecs_brand` (brand_name,sort_order,is_show,brand_type,brand_is_hot) values('"+brand+"','50','1','1','1');"