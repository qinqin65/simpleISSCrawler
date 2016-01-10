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
                semicolonStr = ':'
                print accountInfo[0]
                print accountInfo[1]
                print accountInfo[2]
                print accountInfo[3]
                print
                yield {
                    'address': accountInfo[0][accountInfo[0].find(semicolonStr):],
                    'port': accountInfo[1][accountInfo[1].find(semicolonStr):],
                    'password': accountInfo[2][accountInfo[2].find(semicolonStr):],
                    'encryptionType': accountInfo[3][accountInfo[3].find(semicolonStr):]
                }