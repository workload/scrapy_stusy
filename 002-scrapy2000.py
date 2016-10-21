# -*- coding: utf-8 -*-
import scrapy

from apple.items import AppleItem as DmozItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import  LinkExtractor
from bs4 import BeautifulSoup
from lxml import etree
import re
class DmozSpider(CrawlSpider):
     name = "single"
     start_urls = ["http://esf.hrb.fang.com/housing/__1_0_0_0_1_0_0/"]
     
     def parse(self, response): #http://esf.sh.fang.com/housing/_5920_1_0_0_0_1_0_0/
          for sel in response.xpath('/html/body/div[4]/div[5]/div[4]/div'):
               # item = DmozItem()   /html/body/div[4]/div[5]/div[4]
               # item['name'] = sel.xpath('dl/dd/p[1]/a/text()').extract()[0]
               # item['price'] = sel.xpath('div/p[1]/span[1]/text()').extract()[0]
               url = sel.xpath('dl/dd/p[1]/a/@href').extract()[0]
               yield scrapy.Request(url, callback=self.parse_detail)
               page_links=response.xpath('//*[@id="houselist_B14_01"]/a/text()').extract()
               for link in page_links:
                    if u'下一页' in link:
                         next_link = response.xpath('//*[@id="houselist_B14_01"]/a/@href').extract()[-2]
                         next_link="http://esf.hrb.fang.com" + next_link
                         yield scrapy.Request(next_link, callback=self.parse)
               # //div[@class="houseList"]//

     def parse_detail(self, response):  #http://yijushangcheng.fang.com/
          item = DmozItem()
          re_name = response.xpath('//*[@id="esfbjxq_04"]/text()').extract()[0]
          if u"小区网" in re_name:
               item['name'] = re_name[:-3]
          else:
               item['name'] = re_name

          item['resd1'] = response.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[2]/ul[descendant-or-self::text()]').extract()[0]
          url = response.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/a/@href').extract()[0]
          request = scrapy.Request(url,callback=self.parse_detail2)
          request.meta['item'] = item
          return request


     def parse_detail2(self, response):  #http://yijushangcheng.fang.com/xiangqing/
          item = response.meta['item'] 
          # item['name'] = response.xpath('/html/body/div[4]/div[2]/div[2]/h1/a/text()').extract()[0][:-3]
          item['resd2'] = response.xpath('/html/body/div[4]/div[4]/div[1]/div[2]/div[2]/dl[descendant-or-self::text()]').extract()[0]

          url = response.xpath('//*[@style="width:840px;margin:0 auto;float:none;"]/iframe/@src').extract()[0]
          request = scrapy.Request(url,callback=self.parse_detail3)
          request.meta['item2'] = item
          return request

     def parse_detail3(self, response): #http://esf.sh.fang.com/newsecond/map/NewHouse/NewProjMap.aspx?newcode=1210593112
          item = response.meta['item2']       
          rr = response.xpath('/html/head/script[6][descendant-or-self::text()]').extract()[0]
          com = re.compile(r'px:"(.*?)",py:"(.*?)",isKey') 
          it = re.findall(com,rr)
          # item['coor_x'] = list(it[0])[0]
          # item['coor_y'] = list(it[0])[1]
          item['coor_x'] = it[0][0]
          item['coor_y'] = it[0][1]
          return item

