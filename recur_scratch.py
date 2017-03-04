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
    def __init__(self,savefilename='data.json',savedir='/mnt/hgfs/share/stars'):
        self.datadict = {}
        makedir(savedir)
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
            name = key+str(i)+os.path.splitext(pic)[1]
            pathname = os.path.join(dirpictures,name)
            try:
                download.get(pic,pathname)
            except Exception as e:
                i = i-1
                print e

        dirrelation = os.path.join(dirname,'relation')
        makedir(dirrelation)
        relationdict = valuedict['reletion']
        for rlpic in relationdict.keys():
            rlpicname =rlpic + os.path.splitext( relationdict[rlpic] )[1]
            rlpicpathname = os.path.join(dirrelation,rlpicname)
            try:
                download.get(relationdict[rlpic],rlpicpathname)
            except Exception as e:
                print e
        
        productionslist = valuedict['productions']
        dirproductions = os.path.join(dirname,'productions')
        makedir(dirproductions) 
        filepathname = os.path.join(dirproductions,'productions.txt')
        with open(filepathname,'w') as f:
            for x in range(len(productionslist)):
                productionslist[x] = productionslist[x]+'\n'
                x = x+1

            f.writelines(productionslist)
            

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
        data = extract.get_attr(baikepage,xpath,attrname)
        #extract.print_list(data)

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
        
        datavalue={}
        datavalue["link"] =baikeurl
        datavalue["reletion"] = namedict
        datavalue['pictures'] = piclist
        datavalue['productions'] = productions

        self.datadict[key] = datavalue

        format_json.dict2file(self.datadict,self.savefilename)
        
        #self.do_download(key,datavalue)
        newdatadict={}
        newdatadict[key] = datavalue
        self.queue.put(self.datadict)
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
                #x = random.randrange(0,lenth-1,1)
                #key = keylist[x]
                print 'scratch :'+key
                newkeylist = self.scratch(key)
                self.recu_scratch(newkeylist)

    def downloads(self):
        while True:
            datadict = self.queue.get(True)
            for key in datadict:
                self.do_download(key,datadict[key])

if __name__ == '__main__':
    keylist =[]
    #key = raw_input('input a key: ').decode(sys.stdin.encoding)
    #filename = raw_input('input a file name to save data: ').decode(sys.stdin.encoding)
    key = u'钟欣桐'
    filename = u'log.json'
    keylist.append(key)
    spd = Spider(savefilename=filename)

    proc_scratch = Process(target = spd.recu_scratch,args=(keylist,))
    proc_download = Process(target = spd.downloads, args=())
   
    proc_scratch.start()
    proc_download.start()

    proc_scratch.join()
    proc_download.terminate()
    
