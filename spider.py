#! /usr/bin/env python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sephbaike
import extract
import random
import json
import format_json
import os
import download
from multiprocessing import Process, Queue

def makedir(path):
    if not os.path.exists(path):
        os.mkdir(path)

class Spider():
    def __init__(self,startkeylist,savefilename='data.json',savedir='/mnt/hgfs/share/stars'):
        if not  isinstance(startkeylist,list):
            print 'Init failed.Type error: argument startkeylist should be a list type'
            return
        self.startkeylist = startkeylist
        self.datadict = {}
        makedir(savedir)
        self.savedir = savedir
        self.savefilename = os.path.join(savedir,savefilename)
        self.queue = Queue()

    def do_download(self,key,valuedict,savedir='/mnt/hgfs/share/stars'):
        if not key:
            return
        if not valuedict:
            return
        dirname = os.path.join(savedir,key)
        makedir(dirname)

        dirpictures = os.path.join(dirname,'pictures')
        makedir(dirpictures)
        piclist = valuedict['pictures']
        i=0
        for pic in piclist:
            i = i+1
            #name = key+str(i)+os.path.splitext(pic)[1]
            name = key+str(i)+'.jpg'
            pathname = os.path.join(dirpictures,name)
            try:
                download.get(pic,pathname)
            except Exception as e:
                i = i-1
                print e

        dirrelation = os.path.join(dirname,'relation')
        relationdict = valuedict['reletion']
        download.get_dict(relationdict,dirrelation)

        dirproductions = os.path.join(dirname,'productions')
        producpicdict = valuedict['productions']
        download.get_dict(producpicdict,dirproductions)

    def scratch(self,key):
        #key = raw_input('input a key word: ').decode(sys.stdin.encoding)
        baikeurl =  sephbaike.baike_url(key)
        #print baikeurl
        baikepage = sephbaike.baike(baikeurl)
        #print baikepage

        #print '明星图片'
        xpath = '//a[@class="image-link"]/img'
        attrname = 'data-src'
        piclist = extract.get_attr(baikepage,xpath,attrname)
        #extract.print_list(piclist)

        #print '代表作品'
        xpath = '//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/div'
        attrname = 'title'
        productions = extract.get_attr(baikepage,xpath,attrname)
        #extract.print_list(productions)

        #print '代表作品图片链接'
        xpath = '//div[@class="star-info-block works"]/dl/dd/div/ul/li/a/img'
        attrname = 'src'
        produpiclist = extract.get_attr(baikepage,xpath,attrname)
        #extract.print_list(produpiclist)

        #print '明星关系'
        xpath = '//div[@class="star-info-block relations"]/dl/dd/div/ul/li/a/div'
        attrname = 'title'
        namelist = extract.get_attr(baikepage,xpath,attrname)
        #extract.print_list(namelist)

        #print '明星关系图片链接'
        xpath = '//div[@class="star-info-block relations"]/dl/dd/div/ul/li/a/img'
        attrname = 'src'
        data = extract.get_attr(baikepage,xpath,attrname)
        #extract.print_list(data)
        namedict = {}
        namedict = dict(zip(namelist,data))
        
        produpicdict={}
        produpicdict = dict(zip(productions,produpiclist))
        datavalue={}
        datavalue["link"] =baikeurl
        datavalue["reletion"] = namedict
        datavalue['pictures'] = piclist
        datavalue['productions'] = produpicdict

        self.datadict[key] = datavalue
        
        newdatadict={}
        newdatadict[key] = datavalue
        format_json.dict2file(newdatadict,self.savefilename,mode='a')
        self.queue.put(newdatadict)
        return namelist
    def recu_scratch(self,keylist):
        if not keylist:
            print 'keylist is empty'
            return 
        else:
            lenth = len(keylist)
            if lenth == 1:
                print 'scratch :'+keylist[0]
                newkeylist = self.scratch(keylist[0])
                self.recu_scratch(newkeylist)
            for key in keylist:
                if key in self.datadict:
                    continue
                print 'scratch :'+key
                newkeylist = self.scratch(key)
                self.recu_scratch(newkeylist)

    def downloads(self):
        while True:
            datadict = self.queue.get(True)
            for key in datadict:
                self.do_download(key,datadict[key],savedir=self.savedir)

    def start(self):

        proc_scratch = Process(target = spd.recu_scratch,args=(self.startkeylist,))
        proc_download = Process(target = spd.downloads, args=())
   
        proc_scratch.start()
        proc_download.start()

        proc_scratch.join()
        proc_download.terminate()
    
if __name__ == '__main__':
    
    keylist =[]
    #key = raw_input('input a key: ').decode(sys.stdin.encoding)
    #filename = raw_input('input a file name to save data: ').decode(sys.stdin.encoding)
    key = u'钟欣桐'
    filename = u'log.json'
    keylist.append(key)
    spd = Spider(keylist,savefilename=filename,savedir='/mnt/hgfs/share/stars3')
    spd.start()
