#! /usr/bin/env python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cover


def get(url,outfilename,headers_file = 'headers.json',timeout=5):
    outfile = cover.get_with_headers_file(url,headers_file=headers_file,timeout=timeout)
    with open(outfilename,'w') as f:
        f.write(outfile)

if __name__ == '__main__':
    url = raw_input('input a url : ')
    outfilename = raw_input('input output file name: ').decode(sys.stdin.encoding)
    get(url,outfilename)
