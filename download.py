#! /usr/bin/env python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cover
import os


def get(url,outfilename,headers_file = 'headers.json',timeout=5):
    outfile = cover.get_with_headers_file(url,headers_file=headers_file,timeout=timeout)
    with open(outfilename,'w') as f:
        f.write(outfile)

def get_dict(datadict,dirname):
        if not isinstance(datadict,dict):
            return
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        for key in datadict.keys():
            keyname =key + os.path.splitext( datadict[key] )[1]
            keypathname = os.path.join(dirname,keyname)
            try:
                get(datadict[key],keypathname)
            except Exception as e:
                print e

if __name__ == '__main__':
    url = raw_input('input a url : ')
    outfilename = raw_input('input output file name: ').decode(sys.stdin.encoding)
    get(url,outfilename)
