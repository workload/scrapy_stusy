# -*- coding: utf-8 -*-
# 
#
import scrapy

from apple.items import AppleItem as DmozItem
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup

class DmozSpider(CrawlSpider):
     name = "dmoz3"
     # area_code = ['1646','1639','5278']
     start_urls = ["http://esf.sz.fang.com/housing/_14116_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_316_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_331_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2085_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2083_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_337_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_349_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_352_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_351_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14100_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14099_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_326_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_332_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_336_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_10056_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14117_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14334_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14101_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14103_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14102_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_335_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14104_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_322_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2097_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_10047_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2099_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2094_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14123_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14120_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14105_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14119_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14118_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14106_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_320_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_318_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_329_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_4648_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_339_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_345_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_353_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_323_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_10054_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_4214_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_340_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_350_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14121_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14107_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_319_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_328_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_354_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14333_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_325_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_347_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2091_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14108_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2086_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2082_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_342_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_4800_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_343_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2088_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2087_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2089_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14115_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_344_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_334_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14110_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14109_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_317_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2084_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_327_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_330_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_333_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_346_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_348_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2096_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2098_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2095_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14111_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14112_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_324_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_321_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_341_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2092_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_2093_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_10040_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_338_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14113_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_21974_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14122_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_14114_1_0_0_0_1_0_0/",
               "http://esf.sz.fang.com/housing/_4647_1_0_0_0_1_0_0/"]
     # for i in area_code:
     #      url ="http://esf.sh.fang.com/housing/_"+i+"_1_0_0_0_1_0_0/"
     #      start_urls.append(url)

     def parse(self, response): #http://esf.sh.fang.com/housing/_5255_1_0_0_0_1_0_0/
          for sel in response.xpath('/html/body/div[4]/div[5]/div[4]/div'):
               item = DmozItem()
               item['name'] = sel.xpath('dl/dd/p[1]/a/text()').extract()
               # item['price'] = sel.xpath('div/p[1]/span[1]/text()').extract()[0]
               item['resd1'] = sel.xpath('dl/dd/p[1]/a/@href').extract()
               yield item

               # yield scrapy.Request(url, callback=self.parse_detail)
               # request.meta['item'] = item
               # print item
          page_links=response.xpath('//*[@id="houselist_B14_01"]/a/text()').extract()
          for link in page_links:
               if u'下一页' in link:
                    next_link = response.xpath('//*[@id="houselist_B14_01"]/a/@href').extract()[-2]
                    next_link="http://esf.sz.fang.com" + next_link
                    yield scrapy.Request(next_link, callback=self.parse)
                    return



               
     # def parse_detail(self, response):  #http://yijushangcheng.fang.com/
     #      item = DmozItem()
     #      for res in response.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/a/@href'):
     #           # item = DmozItem()
     #           item['resd1'] = res.extract()
     #           # print res.extract()
     #           return item


