#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import urllib2
import re

from bs4 import BeautifulSoup

baseurl = "http://search.jd.com/Search?keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&pvid=okwe3lui.8o37qo#keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&s=57&click=0"
#伪装浏览器,以免被封
def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req_timeout = 20
    try:
        req = urllib2.Request(url,None,req_header)
        #page = urllib2.urlopen(req,None,req_timeout)
        response = urllib2.urlopen(req)
        html = response.read()
        #html = page
    except urllib2.URLError as e:
        print e.message
    except socket.timeout as e:
        user_agent(url)
    return html

def page_loop(pageid):
    url = baseurl+'&page='+pageid
    print url
    page = user_agent(url)
    #print page
    soup = BeautifulSoup(page)
    total_img = 0
    print "\n\n\n ......\n"
    #print soup.contents
    #img = soup.find_all(['img'])
    #element = soup.find_all('img')
    element = soup.find(id='J_goodsList')
    a=soup.findAll(name='a',attrs={"href":re.compile(r'^//item.jd.com/(.*).html')})
    print "\n\n\n ......\n",a
    for aa in a:
        print aa,"\n"
    index =0
    #element.contents[3]
    print "len",len(element.contents)
    #for myimg in element:
    #    link = myimg.string #get('src')
    #    total_img += 1
         #index=index+1
         #print "\n\n------",index,"\n\n",myimg, "\n\n------"
        #  content2 = urllib2.urlopen(link).read()
        # content2 = user_agent(link).read()
        #这句代码直接从OSC上面弄下来的
        #D:\myimg是保存路径,你可以自己改成自己的,但是路径必须要自己创建好
        #with open(u'D:\myimg'+'/'+link[-11:],'wb') as code:
        #    code.write(content2)
    print total_img
    return total_img
page_start = 1
page_stop = 2
total = 0
#for i in range(page_start,page_stop):
#    total+=page_loop(i)
total+=page_loop(1)
print total
#total就是统计下总共保存到本地的图片数量