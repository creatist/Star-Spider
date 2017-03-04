#! /usr/bin/env python
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from  sephbrowser import SePhBrowser
import json
import format_json
import cover
#import selenium.common.exceptions
def baike(url,type = 'phantomjs',engine = 'baidu',done_xpath= '//a[@class="image-link"]'):
    #print 'in baike()'
    browser = SePhBrowser(type)
    if engine == 'baidu':
        try:
            #print 'browser.get()'
            browser.get(url,timeout = 5)
            #print 'browser.return_page()'  
            page =  browser.return_page(done_xpath,'utf8')
            #page = browser.get_page('utf8')

        except Exception as e:
            page = cover.get_with_headers_file(url)
        finally:
            browser.quit()
        return page
    else:
        browser.quit()
        return 'unknown search engine'


def baike_url(key,type = 'phantomjs',engine = 'baidu',done_xpath= '//h3[@class="t c-gap-bottom-small"]'):
    browser = SePhBrowser(type)
    if engine == 'baidu' :
        browser.baidu(key)
        data = browser.select_one(done_xpath,'utf-8')
        if not data:
            print 'no json data'
            return 
        json_data = format_json.format(data)
        browser.quit()
        return json_data['url']
    else :
        browser.quit()
        print 'unknown search engine'
        return

def baike_picture(url,type = 'phantomjs',engine = 'baidu',done_xpath= '//a[@class="image-link"]'):
    browser = SePhBrowser(type)
    if engine == 'baidu':
        browser.get(url)
        load_done_xpath = '//a[@class="image-link"]'
        page =  browser.return_page(done_xpath,'utf8')
        browser.quit()
        return page
    else:
        browser.quit()
        return 'unknown search engine'
if __name__ == '__main__':
    key = raw_input('input a key word: ').decode(sys.stdin.encoding)
    #key = u'钟欣桐'
    #key = u'古天乐'
    #key = u'胡歌'
    baikeurl =  baike_url(key)
    print baikeurl
    baikepage = baike(baikeurl)
    print baikepage
    
    
