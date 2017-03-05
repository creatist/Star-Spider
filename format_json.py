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

def dict2file(datadict,filename,mode='w',indent=4,ensure_ascii=False):
    datastr = json.dumps(datadict,indent=4,ensure_ascii=False)
    with open(filename,mode) as f:
        f.write(datastr)
    return

def list2dict(name,valuelist):
    i = 0
    valuedict = {}
    for v in valuelist:
        i = i+1
        key = name + str(i)
        valuedict[key] = v

    return valuedict

if __name__ == '__main__':

    source_data = raw_input('input soruce data : ') 
    # {title:'钟欣潼_百度百科',url:'http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin'}    
    # {title:"钟欣潼_百度百科",url:"http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin"} 
    j =  format(source_data)
    print j
    print j["url"]
