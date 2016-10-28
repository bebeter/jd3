pro_url="https://item.jd.com/1334820759.html"
pro_id =pro_url.split(".")[2].replace("com/","")
print pro_id
myimg=u'http://img14.360buyimg.com/n5/jfs/t2254/245/1186857675/137399/53ea98fd/5683a71cN31218a94.jpg'
print myimg.split("/")[-1]#图片名称
print myimg.split("/")[3]#图片大小的 n1 n2




str='''showdesc({"date":1467424688982,"content":"<div style=\"text-align: center;\"> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1669/195/957514410/51008/9cd83d48/55e022e3N7306ff6f.jpg\" height=\"379\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1687/157/1138957458/86658/c5497ab/55e022e3N37ba498c.jpg\" height=\"380\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img10.360buyimg.com/imgzone/jfs/t1300/225/928240908/96649/a079db21/55e4095dN363c163b.jpg\" height=\"430\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img10.360buyimg.com/imgzone/jfs/t1765/310/1306250065/43923/7d473963/55e4095dNfc63a84d.jpg\" height=\"329\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1834/132/1061682913/84060/3c9a509c/55e022e4N80360c13.jpg\" height=\"334\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img10.360buyimg.com/imgzone/jfs/t1741/261/1298798285/122416/66337229/55e4095eN9d67fd62.jpg\" height=\"575\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1708/193/1115545130/112760/55438334/55e022e6N0b5ee723.jpg\" height=\"511\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1705/180/1007698940/78278/37577cad/55e022e7N513bc5e8.jpg\" height=\"511\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1669/205/980133207/123720/85bf9437/55e022e8N36d887e9.jpg\" height=\"511\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img10.360buyimg.com/imgzone/jfs/t1585/261/1155739452/73874/5a4a65e5/55e4095eNf33e0618.jpg\" height=\"554\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1708/213/1117951440/74994/cdf57872/55e022e9Nae155edb.jpg\" height=\"512\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1729/19/1142648570/72025/587fa2d5/55e022eaNa1095270.jpg\" height=\"511\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img11.360buyimg.com/cms/jfs/t1741/11/1096527049/86546/f123dff3/55e022eaN0c4badff.jpg\" height=\"471\" width=\"750\" alt=\"\" /> \n <img data-lazyload=\"//img10.360buyimg.com/imgzone/jfs/t1762/348/1254085044/75432/6a54ea8a/55e4095fN83f347f6.jpg\" height=\"475\" width=\"750\" alt=\"\" /> \n</div><br/>"})'''
str_sub = str.split("\n")
print len(str_sub)
desc_img_url=[]
for s in str_sub:
    desc_url =  s.split("\"")[1]

    if len(desc_url) >10:
        print desc_url
        desc_img_url.append(desc_url)


