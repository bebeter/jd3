#!/usr/bin/env python
#-*- coding: utf-8 -*-


import socket
from pyquery import PyQuery as pq
from lxml import etree
import urllib2
import re
import json


import sys
import urllib
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )




def record(url):

    fn=r"dealed_item_urls.txt"
    f2=open(fn,"w")
    f2.write(url+"\n")
    f2.close()

def getUrls ():
   item_urls=[]
   fn=r"prourl.txt"
   f=open(fn)
   print "\n\n-----------------------------------"
   for line in f.readlines():
      #print line;count
      #if   data.count(line)==0:
      item_urls.append(line.strip())

   item_urls = list(set(item_urls))
   f.close()
   return item_urls



def getDeladUrls ():
   dealed_item_urls=[]
   fn=r"dealed_item_urls.txt"
   f1=open(fn)
   for line in f1.readlines():
       dealed_item_urls.append(line.strip())
   f1.close()

   #print(len(pro_urls))

   return  dealed_item_urls( set(dealed_item_urls))



def getProId(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")
        print pro_id
        return pro_id

def dealPrice ():
   items=[]
   fn=r"d:\jdpro\all_price.txt"
   f=open(fn)
   print "\n\n-----------------------------------"
   for line in f.readlines():
      #print line;count
      #if   data.count(line)==0:
      priceline = line.strip()
      #print priceline
      data = json.loads(priceline)
      #print data[0]['id'].replace("J_",""),data[0]['p'],data[0]['m']
      print "update  `ecs_goods`    set shop_price ='"+data[0]['p']+"' ,market_price ='"+data[0]['m']+"'" \
             "  where seo_goods_title='" + data[0]['id'].replace("J_","")+ "';"
      #item_urls.append()

   items = list(set(items))
   f.close()
   return items


def dealPrice ():
   items=[]
   fn=r"d:\jdpro\all_price.txt"
   f=open(fn)
   print "\n\n-----------------------------------"
   for line in f.readlines():
      #print line;count
      #if   data.count(line)==0:
      priceline = line.strip()
      #print priceline
      data = json.loads(priceline)
      #print data[0]['id'].replace("J_",""),data[0]['p'],data[0]['m']
      print "update  `ecs_goods`    set shop_price ='"+data[0]['p']+"' ,market_price ='"+data[0]['m']+"'" \
             "  where seo_goods_title='" + data[0]['id'].replace("J_","")+ "';"
      #item_urls.append()

   items = list(set(items))
   f.close()
   return items


def dealListDesc ():
   items= getUrls ()
   for item in items:
        getDetail(item)

Fields={}

def getFields ():
    f2=open('D:\jdpro'+'\\txt\\field_name.txt',"r")
    for line in f2.readlines():
        a = line.split(",")
        Fields[a[0]]=a[1]



#产品页面中的产品细节
def getProDetail(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")


        f2=open('D:\jdpro'+'\\txt\\'+str(pro_id)+'\\pro_detail.txt',"r")

        detail = {}

        detail['pid'] = pro_id

        for line in f2.readlines():
                a = line.split("：")
                print a
                if len(a)<2:
                    continue
                '''
                if a[0]=="品牌" :
                    a[0]='brand'
                    a[1]=a[1].replace("♥ 关注","").strip()
                if a[0]=="店铺" :
                    a[0]='dianpu'
                    a[1]=a[1].replace("</a","").split(">")[1].strip()
                if a[0]=="价格" :
                    a[0]="price2"
                    a[1]=a[1].replace("元","") .strip()

                if a[0].find("重")>0 :
                    a[0]="weight"

                if a[0].find("品种")>0 :
                    a[0]="pingzhong"

                if a[0]=="铁皮种类" :
                    a[0]="zhongzhi"

                if a[0]=="包装" :
                    a[0]="baozhuang"

                if a[0]=="营养品种类" :
                    a[0]="fenlei"

                if a[0]=="特产品类" :  #特产品类：云南石斛
                    a[0]="chandi"
                    a[1]=a[1].replace("石斛","") .strip()

                '''
                a[0]=Fields.get(a[0])

                detail[a[0]]=a[1]
        print detail
        for d,v in detail.items():
            print d,v

        print "品牌",detail.get("品牌")
        print "店铺",detail.get("店铺")

        return detail

#列表中的产品细节
def getDetail(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")


        f2=open('D:\jdpro'+'\\txt\\'+str(pro_id)+'\\detail.txt',"r")

        detail = {}

        detail['pid'] = pro_id

        for line in f2.readlines():
                a = line.split("：")
                print a
                if len(a)<2:
                    continue
                detail[a[0]]=a[1]
        print detail
        for d,v in detail.items():
            print d,v


        print "品牌",detail.get("品牌")
        print "店铺",detail.get("店铺")

        return detail

filed=[]
dict={}

def ProDetail(pro_url):
        print "^^^^^^^^^^^^^^^^^^^^^^^^"
        #print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")

        path='D:\jdpro'+'\\txt\\'+str(pro_id)+'\\pro_detail.txt'
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            print path,"not found"
            return


        f2=open(path,"r")

        detail = {}

        detail['pid'] = pro_id




        line_count = 0

        for line in f2.readlines():
                #print line
                a = line.split("：")
                if len(a)<2:
                    print pro_id,line
                    continue
                a[0] = dict.get(a[0])
                detail[a[0]]=a[1]
                line_count=line_count+1
                #countDic(dict,a[0])


        print pro_id,line_count



        '''
        print detail
        for d,v in detail.items():
            print d,v

        print "品牌",detail.get("品牌")
        print "店铺",detail.get("店铺")
        '''
        return detail

def dealProDesc ():
   items= getUrls ()
   for item in items:
        ProDetail(item)




def countDic(dic, key):
    if dic.has_key(key):
        dic[key] += 1
    else:
        dic[key] = 1


def writeUrl(url):

    fn=r"D:\jdpro\redown_url.txt"
    f2=open(fn,"a")
    f2.write(url+"\n")
    f2.close()

def readUrls ():
   item_urls=[]
   fn=r"D:\jdpro\redown.txt"
   f=open(fn)

   for line in f.readlines():
      writeUrl("https://item.jd.com/"+line.strip()+".html")


   f.close()

def doFieldsDict ():
   item_urls=[]
   fn=r"D:\jdpro\field_name.txt"
   f=open(fn)

   for line in f.readlines():
       a=line.strip().split(",")
       dict[a[0].strip()]=a[1].strip()


   f.close()
   print dict




'''
#dealPrice()
dealProDesc()

readUrls ()

for fi in filed:
            print fi

print '++++++++++++++++++'
'''





doFieldsDict()

for key in dict.keys():
           #if(int(dict[key])>100):
             print key, ":" + str(dict[key])

detail0 = ProDetail("https://item.jd.com/10360516087.html")
for key in detail0.keys():
    print key, ":" + str(detail0[key]).strip()
