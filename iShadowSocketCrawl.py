# -*- encoding=utf8 -*-
import sys
import scrapy

reload(sys)
sys.setdefaultencoding("utf-8")

class IShadowSocketCrawl(scrapy.Spider):
    name = 'issInfo'
    start_urls = ['http://www.ishadowsocks.com/']
    
    def parse(self, response):
        for freeInfo in response.css('#free .col-lg-4'):
                accountInfo = freeInfo.xpath('h4/text()').extract()
                print accountInfo[0]
                print accountInfo[1]
                print accountInfo[2]
                print accountInfo[3]
                yield {
                    'address': accountInfo[0],
                    'port': accountInfo[1],
                    'password': accountInfo[2],
                    'encryptionType': accountInfo[3]
                }