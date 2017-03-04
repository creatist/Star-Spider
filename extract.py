#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from lxml import etree
import os
'''
def get_attr(text ,match_xpath,attrname):
    
    html = etree.HTML(text)
    result = html.xpath(match_xpath)
    for r in result:
        data = r.get(attrname)
        yield data
'''
def get_attr(text ,match_xpath,attrname):
    
    html = etree.HTML(text)
    result = html.xpath(match_xpath)
    data = []
    for r in result:
        d = r.get(attrname)
        data.append(d)
    return data
def get_attr_from_file(filename,match_xpath,attrname):
    with open(filename,'r') as f:
        text = f.read()
        return get_attr(text,match_xpath,attrname)

def print_list(lst):
    if isinstance(lst,list):
        for l in lst:
            print l
if __name__ == '__main__':
    #获取百度结果的链接
    #data = get_attr_from_file('baidu.html','//span[@class="c-tools"]','data-tools')

    #获取百科页面的图片链接
    data = get_attr_from_file('baike.html','//a[@class="image-link"]/img','data-src')

    #获取代表作品 xpath = '//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/div' attrname = 'title'
    data = get_attr_from_file('baike-hu.html','//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/div','title')

    #获取代表作品图片链接 xpath = '//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/img' attrname = 'src'
    data = get_attr_from_file('baike.html','//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/img','src')

    #获取明星关系 
    filename = 'baike.html'
    xpath = '//div[@class="star-info-block relations"]/dl/dd/div/ul/li/a/div' 
    attrname = 'title'
    data = get_attr_from_file(filename,xpath,attrname)
 
    #获取明星关系图片链接 
    filename = 'baike.html'
    xpath = '//div[@class="star-info-block relations"]/dl/dd/div/ul/li/a/img' 
    attrname = 'src'
    data = get_attr_from_file(filename,xpath,attrname)
   
    filename = 'amazon.html'
    xpath = '//img[@src]/..'
    attrname = 'href' 
    data = get_attr_from_file(filename,xpath,attrname)
    for d in data:
        print d
