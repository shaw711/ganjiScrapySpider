# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from ganjiScrapySpider.items import HouseItem

class GanjiSpider(CrawlSpider):

    name="ganjiSpider"
    allowed_domains=['ganji.com']
    start_urls=['http://bj.ganji.com/fang1/o1']

    rules=[
       Rule(SgmlLinkExtractor(allow=('http://bj.ganji.com/fang1/o'),restrict_xpaths=('//a[@class="next"]')),
       callback='parse_item',
       follow=True)
    ]

    def parse_start_url(self,response):
    	return self.parse_item(response)

    def parse_item(self,response):
    	sel=Selector(response)
    	houses=sel.xpath('//li[@class="list-img clearfix"]')
    	houseItems=[]
    	for house in houses:
            hItem=HouseItem()
            hItem['title']=house.select('div[@class="list-mod4"]/div[@class="info-title"]/a/text()').extract()[0]
            hItem['name']=house.select('div[@class="list-mod4"]/div[@class="list-mod2"]/div[@class="list-word"]/span[@class="list-word-col"]/a/text()').extract()[0]
            hItem['price']=house.select('div[@class="list-mod4"]/div[@class="list-mod3 clearfix"]/p[@class="list-part"]/em[@class="sale-price"]/text()').extract()[0]
            houseItems.append(hItem)
        return houseItems