from selenium import webdriver

def init_phantomjs_driver(*args, **kwargs):
    print 'init...'
    headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Connection': 'keep-alive'
    }

    for key, value in headers.iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

    driver =  webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400,1000)
    
    print 'init done'
    return driver


def main():
    service_args = [
        '--proxy=127.0.0.1:9999',
        '--proxy-type=http',
        '--ignore-ssl-errors=true'
        ]

    driver = init_phantomjs_driver(service_args=service_args)

    driver.set_page_load_timeout(10)
    driver.get('http://baike.baidu.com/item/%E9%92%9F%E6%AC%A3%E6%BD%BC/9794318?fr=aladdin')
    print dirver.page_source.encode('utf8')

if __name__ == '__main__':
    main()
