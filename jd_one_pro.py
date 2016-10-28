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

'''
pro_id=""
pro_txt=[]
pro_urls=[]
pro_img = []  #产品小图片
desc_img_url=[] #产品描述图篇链接
descContent=[]
'''

def record(url):

    fn=r"downed_data.txt"
    f2=open(fn,"a")
    f2.write(url+"\n")
    f2.close()

def getUrls ():
   item_urls=[]
   fn=r"alldata.txt"
   f=open(fn)
   print "\n\n-----------------------------------"
   for line in f.readlines():
      #print line;count
      #if   data.count(line)==0:
      item_urls.append(line.strip())

   item_urls = list(set(item_urls))

   downed_item_urls=[]
   fn=r"downed_data.txt"
   f1=open(fn)
   for line in f1.readlines():
       downed_item_urls.append(line.strip())
   f1.close()

   #print(len(pro_urls))
   f.close()
   return  list(set(item_urls) - set(downed_item_urls))




'''
for i in range(0,len(pro_urls)):
    print i,pro_urls[i]
'''



#创建新目录
def mkdir(path):
    import os
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False



def user_agent(url):

    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    req_timeout = 20
    try:
        req = urllib2.Request(url,None,req_header)
        #page = urllib2.urlopen(req,None,req_timeout)
        response = urllib2.urlopen(req)

        html = response.read()
        print html.decode('GBK','ignore')

        #html = page
    except urllib2.URLError as e:
        print e.message
    except socket.timeout as e:
        user_agent(url)
    return html

def getAllImg(page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        #个人信息页面所有代码
        content = re.search(pattern,page)
        #从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg,content.group(1))
        return images

def getDesc(content):
   # desc: '//d.3.cn/desc/10037592988?cdn=2',
   patternLink = re.compile('d.3.cn//desc//(.*?)"',re.S)
   desc_link = re.findall(patternLink,content.group(1))
   return desc_link

def page_loop(pro_id,pro_url):

    url = pro_url

    f3=open("pro.txt","a")
    f3.write(url+"\n")
    f3.close()

    print url
    page = user_agent(url)



    fcont=open("d:\\jdpro\\pro\\"+str(pro_id)+".html","a")
    fcont.write(page)
    fcont.close()



    #print page
    doc = pq(page)
    #doc=pq(filename="d:\\kk.html")
    total_img = 0
    print "down pro page..\n\n\n ......\n"



    #print soup.contents
    #img = soup.find_all(['img'])
    #element = soup.find_all('img')
    #element = soup.find(id='J_goodsList')
    #a=soup.findAll(name='a',attrs={"href":re.compile(r'^//item.jd.com/(.*).html')})
    #print doc.html()
    #print type(doc)


    #print "\n\n\n ......\n",a
    #找到产品图
    ul = doc('ul.lh')
    print "len",len(ul)
    if len(ul)==0:
        print(u"不能取到产品图片。")
        return

    print "\n 共有产品图：",len(pq(ul[0]).find('img'))
    pro_img=[]
    for aa in ul[0]:

        for k in range(len(pq(aa).find('img'))):
            pro_img.append("http:"+pq(aa).find('img').eq(k).attr('src'))
            print pq(aa).find('img').eq(k).attr('src')
        '''
        print pq(aa).find('img').eq(0).attr('src')
        print pq(aa).find('img').eq(1).attr('src')
        print pq(aa).find('img').eq(2).attr('src')
        print pq(aa).find('img').eq(3).attr('src')
        print pq(aa).find('img').eq(4).attr('src')
        if pq(aa).find('img').eq(0).attr('src') is None :
            break
        pro_img.append("http:"+pq(aa).find('img').eq(0).attr('src'))
        pro_img.append("http:"+pq(aa).find('img').eq(1).attr('src'))
        pro_img.append("http:"+pq(aa).find('img').eq(2).attr('src'))
        pro_img.append("http:"+pq(aa).find('img').eq(3).attr('src'))
        pro_img.append("http:"+pq(aa).find('img').eq(4).attr('src'))
        '''

    downProImg (pro_id,pro_img)
        #print pq(aa).find('a').eq(0).html()
        #print pq(aa).find('i').eq(0).text()

        #pname=pq(aa).find('em').eq(1).text()
        #print pname.replace(" ","")
        #.replace_all("<font class=\"skcolor_ljg\">","").replace_all("</font>","")
        #print pq(aa).find('img').eq(0).attr('src')#

        #pro_url = pq(aa).find('a').eq(0).attr('href')
        #print pro_url
        #print pq(aa).find('i').eq(1).html()
        #if len(pro_url)<50:
        #    pro_url="http:"+pro_url
        #pro.append(pro_url)
        #print len(pro)
    '''
    print "detail is :"
    detail_div = doc('div#J-detail-content')
    print detail_div.html()
    print detail_div.find('img').eq(0).attr('src')
    for img in   detail_div.find('img'):
        print img.attr('src')
    '''
    detail_div = doc('img#spec-img')
    print "pro name ",detail_div.attr('alt')
    pname = doc('div.p-name').text()

    print "pname" ,pname



    ul_para = doc('ul#parameter-brand')
    pro_txt=[]

    lis = pq(ul_para).find('li')
    print len(lis)
    for k in range(len(pq(ul_para).find('li'))):
        print lis.eq(k).text()
        pro_txt.append(lis.eq(k).text())

    ul_para = doc('ul.parameter2')

    lis = pq(ul_para).find('li')
    print len(lis)
    for k in range(len(pq(ul_para).find('li'))):
        print lis.eq(k).text()
        pro_txt.append(lis.eq(k).html())

    downProDescTxt(pro_id,pro_txt)       #下载保存文字描述 价格

    #取得描述的链接
    #desc_link = getDesc(page)
    #desc: '//d.3.cn/desc/10037592988?cdn=2',
    #desc: \'//dx.3.cn/desc/1171159228?cdn=2\'
    patternLink = re.compile('desc: \'(.*?)\'',re.S)
    desc_link = re.findall(patternLink,page)
    desc_url= "http:"+desc_link[0]
    print desc_url

    descContent=[]
    desc_img_url=[]#产品描述中的图片
    desc_str = user_agent(desc_url)
    print desc_str
    descContent.append(desc_str)  #产品描述的源码html部分
    str_sub = desc_str.split("\\")
    for s in str_sub:
        if len(s)>30 and s.find("jpg")>0 :
            print s.replace("\"","")
            desc_img_url.append("http:"+s.replace("\"",""))

    downProDescImg(pro_id,desc_img_url,descContent)


    '''
    data = json.loads("["+desc_str[9:-1]+"]")
    print data[0]
    desc_str=data[0]['content']
    descContent.append(desc_str)
    str_sub = desc_str.split("\n")#.replace("\\","")
    print len(str_sub)

    for s in str_sub:
       print s

       if len(s) >10:
           desc_url =  s.split("\"")[1]
           print desc_url
           if len(desc_url) >30:
                desc_img_url.append("http:"+desc_url)
    '''
    for s in desc_img_url:
        print s


    index =0
    #element.contents[3]


    #print total_img
    return total_img








page_start = 1
page_stop = 71
total = 0


def main():
   items = getUrls ()

   for item in items[0:2]:


        dodown(item)
        record(item)


'''
for i in range(page_start,page_stop):
    total+=page_loop(i)
    print "Page:",i
'''


def downProImg (pro_id,pro_img):
    img_index=0
    for myimg in pro_img:
        #    link = myimg.string #get('src')
        #    total_img += 1
              img_index=img_index+1
              myimg=myimg.replace('/n5/','/n1/')
              #print "\n\n------","\n\n",myimg, "\n\n------"
              content2 = urllib2.urlopen(myimg).read()

              #content2 = user_agent(myimg).read()
            #这句代码直接从OSC上面弄下来的
            #D:\myimg是保存路径,你可以自己改成自己的,但是路径必须要自己创建好
              with open('D:\jdpro'+'\\'+pro_id+'\\'+str(img_index)+"."+myimg.split(".")[-1],'wb') as code:
                code.write(content2)

    f2=open('D:\jdpro'+'\\'+pro_id+'\\'+'pro.txt',"a")
    for url in pro_img:
       f2.write(url+"\n")
    f2.close()


def downProDescImg(pro_id,desc_img_url,descContent):
    img_index=0
    print 'desc img',len(desc_img_url)
    for myimg in desc_img_url:
        img_index=img_index+1
        #print "\n\n------","\n\n",myimg, "\n\n------"
        content2 = urllib2.urlopen(myimg).read()
        with open('D:\jdpro'+'\\'+pro_id+'\\d'+str(img_index)+".jpg",'wb') as code:
                code.write(content2)#+myimg.split(".")[-1]

    f2=open('D:\jdpro'+'\\'+pro_id+'\\'+'desc.txt',"a")
    for url in desc_img_url:
           f2.write(url+"\n")
    f2.close()

            #print(descContent[0])
    if len(descContent)==0:
        return
    f2=open('D:\jdpro'+'\\'+pro_id+'\\'+'pro_desc.txt',"a")
    f2.write(descContent[0])
    f2.close()


def downProDescTxt(pro_id,pro_txt):

    price_url ="http://p.3.cn/prices/mgets?skuIds=J_"+pro_id+"&type=1"
    data = json.loads(user_agent(price_url))
    print data[0]['p']


    f2=open('D:\jdpro'+'\\'+pro_id+'\\'+'pro_detail.txt',"a")
    for txt in pro_txt:
       f2.write(txt+"\n")
    f2.write("价格："+data[0]['p']+"元")
    f2.close()



def createProDir(pro_id):
    mkdir("d:\\jdpro\\"+pro_id)


def dodown(pro_url):
        print pro_url
        pro_id =pro_url.split(".")[2].replace("com/","")
        print pro_id
        #pro_url="http://item.jd.com/10271997395.html"
        createProDir(pro_id)

        page_loop(pro_id,pro_url)



        #print total
        #total就是统计下总共保存到本地的图片数量



















if __name__ == '__main__':
    main()