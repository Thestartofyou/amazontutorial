# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011']

    def parse(self, response): 
        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract() 
        product_imagelink= response.css('.s-image , #nav-cover::attr(src)').extract()
        
        items['product_name'] = product_name
        items['product_imagelink'] = scrapy.Field()
        
        yield items
