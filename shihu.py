#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import urllib
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import traceback
import sys
import glob
reload(sys)
sys.setdefaultencoding( "utf-8" )
sel=webdriver.Chrome()




def login():

    loginurl = 'http://www.123shihu.com/123shihu2016adm'
    #open the login in page
    sel.get(loginurl)
    time.sleep(1)

    #sign in the username
    try:
        sel.find_element_by_xpath("/html/body/div/form/p[1]/label/input").send_keys('sunxiaoning')
        print 'user success!'
    except:
        print 'user error!'
    time.sleep(1)
    #sign in the pasword
    try:
        sel.find_element_by_xpath("/html/body/div/form/p[2]/label/input").send_keys('sunxiaoning19996240')
        print 'pw success!'
    except:
        print 'pw error!'

    try:
        sel.find_element_by_xpath("/html/body/div/form/p[3]/label/input").send_keys('ly_123shihu')
        print ' success!'
    except:
        print 'qy error!'

    sel.find_element_by_xpath("/html/body/div/form/p[4]/input[1]").click()

    time.sleep(1)





def goList():
    homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=list"
    sel.get(homeurl)


def goAdd():
    homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=add"
    sel.get(homeurl)



def getCookie():
    #get the session cookie
    cookie = [item["name"] + "=" + item["value"] for item in sel.get_cookies()]
    #print cookie
    cookiestr = ';'.join(item for item in cookie)
    print cookiestr

def getUrls ():
   item_urls=[]
   fn=r"all_pro.txt"
   f=open(fn)
   print "\n\n-----------------------------------"
   for line in f.readlines():
      #print line;count
      #if   data.count(line)==0:
      item_urls.append(line.strip())

   item_urls = list(set(item_urls))

   downed_item_urls=[]
   fn=r"dealed_pro.txt"
   f1=open(fn)
   for line in f1.readlines():
       downed_item_urls.append(line.strip())
   f1.close()

   #print(len(pro_urls))
   f.close()
   return  list(set(item_urls) - set(downed_item_urls))



def main():
   #items = getUrls ()
   login()

   items=["https://item.jd.com/1129481.html"]
   time.sleep(3)
   index =1
   for item in items:
        print "处理第：",index

        detail1={}
        detail2={}


        detail1 = getProDetail(item)#产品页面
        detail2 = getDetail(item)#列表页面

        pname = detail2.get('pname')#产品名
        pro_id=detail2.get('pid')

        tab1(detail1,detail2)

        getProImg(item)


        prodesc = doProDescUrl(pro_id,getProDesc(item),pname)

        #tab2(prodesc)

        #record(item)
        index=index+1





def recordId(pid,jdid):

    fn=r"pro_ids.txt"
    f2=open(fn,"a")
    f2.write(pid+","+jdid+"\n")
    f2.close()



def record(url):

    fn=r"dealed_pro.txt"
    f2=open(fn,"a")
    f2.write(url+"\n")
    f2.close()


'''
品牌： 霍之宝 ♥ 关注
商品名称：霍之宝 霍山铁皮石斛花铁皮枫斗花20克/罐 应季新花
商品编号：1334820759
店铺： <a href="//huozhibao.jd.com" target="_blank">七宝堂保健品专营店</a>
商品毛重：27.00g
商品产地：中国大陆
货号：铁皮石斛花
铁皮种类：种植
营养品种类：铁皮
分类：其它
特产品类：霍山石斛
包装：罐装
价格：145.00元
'''
#产品页面中的产品细节
def getProDetail(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")


        f2=open('D:\jdpro'+'\\txt\\'+str(pro_id)+'\\pro_detail.txt',"r")

        detail = {}

        for line in f2.readlines():
                a = line.split("：")
                print a
                if len(a)<2:
                    continue
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

def getProImgname(prourl):
   for  i  in glob.glob(".\\*.txt"):
        print i


def getProId(pro_url):
    print pro_url
    pro_id =pro_url.split(".")[2].replace("com/","")
    return pro_id


def getProImg(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")


        f2=open('D:\jdpro'+'\\txt\\'+str(pro_id)+'\\pro.txt',"r")

        ProImg = []

        for line in f2.readlines():
            print line
            ProImg.append(line)
        f2.close()
        return ProImg


def doProLocalpath(pro_id,imgs):
    imgPath=[]
    for index in range(1,len(imgs)):
        imgPath.append("'D:\jdpro'+'\\txt\\'+str(pro_id)"+str(index+1)+".jpg")
    return imgPath



def doProDescUrl(pid,imgs,pname):
    url0=r'/images/pro/' +  str(pid)+'/d'
    urls=""
    url=""
    if pname is None:
        pname = ''

    for index in range(1,len(imgs)):
          url = '<img src="'  + url0+ str(index+1)+'.jpg" title="'+pname+'" alt="'+pname+'" />'
          urls= urls+url
    print urls,"\n"
    return  urls


def getProDesc(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")


        f2=open('D:\jdpro'+'\\txt\\'+str(pro_id)+'\\desc.txt',"r")

        ProImgDesc = []

        for line in f2.readlines():
            print line
            ProImgDesc.append(line)
        f2.close()
        return ProImgDesc






def tab1(detail1,detail2):
    homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=add"
    sel.get(homeurl)
    time.sleep(3)

    print "tab 1 ...."


    pid=detail2.get('pid')
    pname = detail2.get('pname')#产品名
    title = detail2.get('title')#标题
    price = detail2.get('price')#价格

    brand = detail1.get('brand')#品牌
    dianpu = detail1.get('dianpu')#店铺
    weight = detail1.get('weight')#重量
    pingzhong = detail1.get('pingzhong')#紫皮
    zhongzhi =  detail1.get('zhongzhi')#种植方式
    fenlei =  detail1.get('fenlei')#分类  风斗
    baozhuang = detail1.get('baozhuang')#包装
    price2 = detail1.get('price2')
    chandi = detail1.get('chandi')
    mprice = detail1.get('mprice')

    if pname is None :
        pname =  detail1.get('pname')# 产品名

    if pname is None :
        pname = "产品名称"# 产品名

    print pname,"1111"
    pname = unicode("产品名称",'UTF-8')

    try:
        nameInput = sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[1]/td[2]/input[1]')
        nameInput.send_keys(pname)


        #sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[4]/td[2]/select').send_keys(fenlei)

        #sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[6]/td[2]/select').send_keys(brand)


        sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[7]/td[2]/input[1]').send_keys(price)
        sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[9]/td[2]/input').send_keys(title) #商品标签：
        sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[10]/td[2]/input').send_keys(pid)#商品SEO标题：
       # //*[@id="general-table"]/tbody/tr[10]/td[2]/input
       #general-table > tbody > tr:nth-child(10) > td:nth-child(2) > input[type="text"]





        '''
        brand=sel.find_element_by_name('brand_id')
        #Select(brand).select_by_value('0')
        Select(brand).select_by_visible_text(brand)
        brand.find_element_by_xpath()
        '''


        sel.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()#提交


        homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=list"
        sel.get(homeurl)

        editpage = sel.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[12]/a[2]').get_attribute("src")      #提交
        sel.get(editpage)

        gid = editpage.split('&')[3].replace("goods_id=","")


        recordId(pid,gid)


        print 'set value success!'
    except  :
        print ' tab1  set value error!'
        traceback.print_exc()





def tab2(imgdesc):

    #homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=list"
    #sel.get(homeurl)

    #click to login


    sel.find_element_by_xpath('//*[@id="detail-tab"]').click()#  tab 页



    try:
        sel.find_element_by_xpath('//*[@id="detail-table"]/tbody/tr/td/div/div[1]/span[1]/span').click()
        sel.find_element_by_xpath('//*[@id="detail-table"]/tbody/tr/td/div/div[2]/textarea').send_keys(imgdesc)

        print 'click success!'
    except:
        print 'click error!'

    time.sleep(1)



def tab3():

    homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=list"
    sel.get(homeurl)

    #click to login
    try:
        sel.find_element_by_xpath("/html/body/div/form/p[4]/input[1]").click()
        print 'click success!'
    except:
        print 'click error!'

    time.sleep(1)





def tab4():

    homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=list"
    sel.get(homeurl)

    #click to login
    try:
        sel.find_element_by_xpath("/html/body/div/form/p[4]/input[1]").click()
        print 'click success!'
    except:
        print 'click error!'

    time.sleep(1)


def tab5():

    homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=list"
    sel.get(homeurl)

    #click to login
    try:
        sel.find_element_by_xpath("/html/body/div/form/p[4]/input[1]").click()
        print 'click success!'
    except:
        print 'click error!'

    time.sleep(1)





if __name__ == '__main__':
    main()













'''

pname="111"

pcat=""#产品分类
brand=""#品牌
price=""
biao =""
seo=""







time.sleep(1)

'''

'''
import urllib2


print '%%%using the urllib2 !!'
homeurl = sel.current_url
print 'homeurl: %s' % homeurl

headers = {'cookie':cookiestr}
req = urllib2.Request(homeurl, headers = headers)
try:
    response = urllib2.urlopen(req)
    text = response.read()


    fd = open('homepage', 'w')
    fd.write(text)
    fd.close()
    print '###get home page html success!!'
except:
    print '### get home page html error!!'

'''