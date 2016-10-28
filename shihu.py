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
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
sel=webdriver.Chrome()

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


time.sleep(1)
#click to login
try:
    sel.find_element_by_xpath("/html/body/div/form/p[4]/input[1]").click()
    print 'click success!'
except:
    print 'click error!'

time.sleep(1)

#get the session cookie
cookie = [item["name"] + "=" + item["value"] for item in sel.get_cookies()]
#print cookie

cookiestr = ';'.join(item for item in cookie)
print cookiestr


homeurl="http://www.123shihu.com/123shihu2016adm/goods.php?act=add"
sel.get(homeurl)


pname="111"

pcat=""#产品分类
brand=""#品牌
price=""
biao =""
seo=""

try:
    sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[1]/td[2]/input[1]').send_keys(pname)
    sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[4]/td[2]/select').send_keys(pcat)

    sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[6]/td[2]/select').send_keys(brand)
    sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[7]/td[2]/input[1]').send_keys(price)
    sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[9]/td[2]/input').send_keys(biao) #商品标签：
    sel.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[10]/td[2]/input').send_keys(seo)#商品SEO标题：
    sel.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()#提交

    # 后退


    #第二页
    sel.find_element_by_xpath('//*[@id="detail-tab"]').click()
    sel.find_element_by_xpath('//*[@id="detail-table"]/tbody/tr/td/div/div[1]/span[1]/span').click()
    sel.find_element_by_xpath('//*[@id="detail-table"]/tbody/tr/td/div/div[2]/textarea').send_keys(brand)
    sel.find_element_by_xpath('//*[@id="detail-table"]/tbody/tr/td/input').click()



    print 'set value success!'
except:
    print 'set value error!'





time.sleep(1)



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

