#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
from pyquery import PyQuery as pq
from lxml import etree
import urllib2
import re






pro=[]
#baseurl ="d:\\kk.html"
#伪装浏览器,以免被封
def user_agent(url):

    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
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
    pageno= 2*pageid-1
    pagestart = pageid*60 -60
    if pageid ==1:
        page_start = 1
    baseurl = "http://search.jd.com/Search?keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&s=57&click=0&page=1#keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&qrst=1" \
              "&rt=1&stop=1&vt=2&page="+str(pageno)+"&s="+str(pagestart)+"&click=0"

    url = baseurl+'&page='+str(pageid)
    url="http://search.jd.com/Search?keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=5&s=120&click=0#keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=17&s=480&click=0"
    f3=open("page.txt","a")
    f3.write(url+"\n")
    f3.close()
    print url
    page = user_agent(url)
    #print page
    doc = pq(page)
    #doc=pq(filename="d:\\kk.html")
    total_img = 0
    print "\n\n\n ......\n"
    #print soup.contents
    #img = soup.find_all(['img'])
    #element = soup.find_all('img')
    #element = soup.find(id='J_goodsList')
    #a=soup.findAll(name='a',attrs={"href":re.compile(r'^//item.jd.com/(.*).html')})
    #print doc.html()
    #print type(doc)

    li = doc('li.gl-item')
    a  = doc('a')
    print "\n\n\n ......\n",a
    print "len",len(li)
    for aa in li:
        print "\n"
        #print pq(aa).find('a').eq(0).html()
        #print pq(aa).find('i').eq(0).text()

        #pname=pq(aa).find('em').eq(1).text()
        #print pname.replace(" ","")
        #.replace_all("<font class=\"skcolor_ljg\">","").replace_all("</font>","")
        #print pq(aa).find('img').eq(0).attr('src')#

        pro_url = pq(aa).find('a').eq(0).attr('href')
        print pro_url
        #print pq(aa).find('i').eq(1).html()
        if len(pro_url)<50:
            pro_url="http:"+pro_url
        pro.append(pro_url)
        print len(pro)
    index =0
    #element.contents[3]

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
    #print total_img
    return total_img
page_start = 1
page_stop = 71
total = 0

'''
for i in range(page_start,page_stop):
    total+=page_loop(i)
    print "Page:",i
'''
total+=page_loop(1)
print total
#total就是统计下总共保存到本地的图片数量


f2=open("alldata.txt","a")
print "pro_len !!!!!!!!!!!!!!!!!!!!!!!",len(pro)
for url in pro:
   f2.write(url+"\n")
f2.close()