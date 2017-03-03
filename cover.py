import requests
import os
import json

#with open('headers.json','r') as f:
#    headers = f.read()
#    url = 'http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin'
#    r = requests.get(url,headers=json.loads(headers),timeout = 10)
#    #print r.headers
#    print r
#    #print type(r)
#    print r.content


def get_with_headers(url,headers,timeout=10):
    r = requests.get(url,headers=headers,timeout=timeout)
    return r.content


def get_with_headers_file(url,headers_file='headers.json',timeout=10):
    with open(headers_file,'r') as f:
        headers_str = f.read()
        headers = json.loads(headers_str)
        return get_with_headers(url,headers=headers,timeout=timeout)


if __name__ == '__main__':
    headers_file = 'headers.json'
    url = 'http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin'
    print get_with_headers_file(url)
