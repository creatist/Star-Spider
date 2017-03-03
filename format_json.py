#! /usr/bin/env python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import json

def format(source_data):
    source = source_data
    re_item = re.compile(r'(?<=[{,])\w+')
    out = re_item.sub("\"\g<0>\"", source)
    out = out.replace("\'","\"")
    l = json.loads(out)
    return l

if __name__ == '__main__':

    source_data = raw_input('input soruce data : ') 
    # {title:'钟欣潼_百度百科',url:'http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin'}    
    # {title:"钟欣潼_百度百科",url:"http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin"} 
    j =  format(source_data)
    print j
    print j["url"]
