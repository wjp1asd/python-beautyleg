# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,HtmlResponse
from leg.items import LegItem

 
class LegspiderSpider(scrapy.Spider):
    name = 'legspider'
    #allowed_domains = ['http://mm.lushi2022.com/','http://lvxing666.com/']
    start_urls = []
    for i in range(1,1000):
        start_urls.append('http://www.beautyleg.com/sample.php?no='+str(i))
        
    def parse(self, response):
      ll= LegItem()
      legs = response.xpath("//img/@src").extract()
      print(legs)
      ll['pic'] = legs 
      return ll

