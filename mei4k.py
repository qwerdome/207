import requests
import time
from lxml import etree
import os
#http://pic.netbian.com/4kmeinv/index_3.html
dirnames = 'mei4k'
if not os.path.exists(dirnames):
    os.mkdir(dirnames)
for number in range(1,3):
    if number==1:
        url = 'http://pic.netbian.com/4kmeinv/'
    else:
        url='http://pic.netbian.com/4kmeinv/index_{}.html'.format(number)

    headers ={'User-Agent':'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)'}
    page= requests.get(url=url,headers=headers)
    page.encoding='gbk'
    response = page.text
    tree = etree.HTML(response)
    div_list = tree.xpath('//div[@class="slist"]//li')
    for li in div_list:
        name = li.xpath('./a/img/@alt')[0]+'.jpg'
        wangye = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        imgpath = dirnames+'/'+name
        img_data=requests.get(url=wangye,headers=headers).content
        with open(imgpath,'wb') as fp:
            fp.write(img_data)
