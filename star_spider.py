#! /usr/bin/env python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sephbaike
import extract

key = raw_input('input a key word: ').decode(sys.stdin.encoding)
baikeurl =  sephbaike.baike_url(key)
print baikeurl
baikepage = sephbaike.baike(baikeurl)
print baikepage

print '明星图片'
xpath = '//a[@class="image-link"]/img'
attrname = 'data-src'
data = extract.get_attr(baikepage,xpath,attrname)
extract.print_list(data)

print '代表作品'
xpath = '//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/div'
attrname = 'title'
data = extract.get_attr(baikepage,xpath,attrname)
extract.print_list(data)

print '代表作品图片链接'
xpath = '//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/img'
attrname = 'src'
data = extract.get_attr(baikepage,xpath,attrname)
extract.print_list(data)

print '明星关系'
xpath = '//div[@class="star-info-block relations"]/dl/dd/div/ul/li/a/div'
attrname = 'title'
data = extract.get_attr(baikepage,xpath,attrname)
extract.print_list(data)
print '明星关系图片链接'
xpath = '//div[@class="star-info-block relations"]/dl/dd/div/ul/li/a/img'
attrname = 'src'
data = extract.get_attr(baikepage,xpath,attrname)
extract.print_list(data)
