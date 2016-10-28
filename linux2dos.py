# -*- coding: utf-8 -*-
#encoding=utf-8
import os
import re
def getListFiles(path):
  assert os.path.isdir(path), '%s not exist.' % path
  ret = []
  for root, dirs, files in os.walk(path):
    #print '%s, %s, %s' % (root, dirs, files)
    for filespath in files:
      ret.append(os.path.join(root,filespath))
  return ret
ret = getListFiles(r'F:\ts\seo\file\123yinger')
print "file count:",len(ret)
index =0
for f in ret[:]:
    print index,f,"\n"
    index=index+1
    if index > 2:
        break
    fRead = open(f,'rU')
    #f=f.replace("file",'wfile')
    fWrite = open(r"F:\ts\seo\wfile\123yinger\123yinger_all.txt",'a')
    try:
         for line in fRead.readlines():
             #print "line:",line
             #fWrite.write(line[:-1]+"\r\n")
             # fWrite.write(line[:-1])
             r1 = 'href=" *javascript:if\(confirm\(\'(htt[^"\s]*).*?""'
             line = re.sub(r1, 'href="$1"', line)
             fWrite.write(line)
    finally:
        fRead.close()
        fWrite.close()

    fRead.close()
    fWrite.close()
