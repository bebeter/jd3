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
driver=webdriver.Chrome()



def getBrand():

    #brand
    ##J_selector > div.J_selectorLine.s-brand > div > div.sl-ext > a.sl-e-more.J_extMore
    driver.find_elements_by_xpath('//*[@id="J_selector"]/div[1]/div/div[3]/a')[0].click()
    time.sleep(3)
    brands=driver.find_elements_by_xpath('//ul[@class="J_valueList v-fixed"]/li/a')
    print len(brands)
    for b in range(0,len(brands)):
        #print brands[b].text()
        html =driver.execute_script("return arguments[0].innerHTML;", brands[b])
        print html





def getLink():
    pro_links=driver.find_elements_by_tag_name('a')
    f2=open("alldata.txt","a")
    #WebElement
    print len(pro_links)
    lasturl=""
    for link in pro_links:
        link_url=str(link.get_attribute('href'))
        if link_url.find("item")>1:
            if link_url.find("comment") <0:
                if link_url==lasturl:
                    continue
                else:
                    lasturl = link_url
                    print link_url
                    f2.write(link_url+"\n")
    f2.close()

def moveWindow():

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*2/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*3/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*4/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*5/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*6/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*7/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*8/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*9/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*7/10)")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*5/10)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*3/10)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-800);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-200);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-600);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-300);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-400);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-500);")
    #将页面滚动条拖到底部
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(3)

    #将滚动条移动到页面的顶部
    js="var q=document.documentElement.scrollTop=10"
    driver.execute_script(js)
    time.sleep(3)

def main():
    #获取参数
    url="https://search.jd.com/Search?keyword=%E7%9F%B3%E6%96%9B&enc=utf-8&wq=%E7%9F%B3%E6%96%9B&pvid=ntlc2oui.8o37qo"#sys.argv[1]
    #url="https://item.jd.com/1124152398.html"
    #操作IE

    #driver = webdriver.Firefox()
    driver.get(url)
    print driver.page_source

    driver.maximize_window()
    moveWindow()


    #driver.find_element_by_xpath("//*[@id='wrapper_wrapper']").send_keys(Keys.DOWN)


    f2=open('D:\jdpro'+'\\page\\1.html',"a")
    f2.write(driver.page_source)
    f2.close()

    #翻页
    #driver.find_element_by_class_name("fp-next").click()
    #print driver.page_source
    for i in range(0,34):
        driver.find_element_by_class_name("fp-next").send_keys(Keys.ARROW_RIGHT)
        moveWindow()
        time.sleep(3)
        print driver.page_source
        time.sleep(3)
        f2=open('D:\jdpro'+'\\page\\'+str(i)+'.html',"a")
        f2.write(driver.page_source)
        f2.close()
        getLink()


    #创建目录



    if 2>1 :
        return
    dir_name='t'
    print dir_name
    root_dir='d:\\img'
    dir_name=root_dir+'\\'+dir_name
    dir_name=dir_name.replace('|','-')
    if(os.path.exists(root_dir)!=True):
        os.mkdir(root_dir)
    if(os.path.exists(dir_name)!=True):
        os.mkdir(dir_name)
    images=driver.find_elements_by_tag_name('img')
    count=0
    #cheeses = driver.find_elements(By.CLASS_NAME, "p-parameter")
    cheeses = driver.find_elements_by_class_name("p-parameter")
    ActionChains(driver).move_to_element(cheeses)
    print(len(images))
    for image in images:
        im=driver.find_elements_by_partial_link_text(str(image.get_attribute('src')))

        count=count+1
        image_url=str(image.get_attribute('src'))


        if image_url is None :
            print count,image_url,"1"
            continue
        else:
            print count,image_url
        try:
            img_file=urllib.urlopen(image_url)
        except IOError:
            continue
        byte=img_file.read()
        print count,'donwload complete!','-'*10,'size:',byte.__len__()/1024,'KB'
        if(byte.__len__()>7000):
            file_name=image_url.replace('/','_')
            file_name=file_name.replace(':','_')
            end=file_name.__len__()
            if(file_name.rfind('!')!=-1):
                end=file_name.rfind('!')
            if(file_name.rfind('?')!=-1):
                end=file_name.rfind('?')
            file_name=file_name[:end]
            write_file=open(dir_name+'\\'+file_name,'wb')
            write_file.write(byte)
            write_file.close()
            print count,file_name,'complete!'
    driver.quit()
if __name__ == '__main__':
    main()