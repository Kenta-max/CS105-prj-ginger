# -*- coding: utf-8 -*-

import scrapy


class RankingSpider(scrapy.Spider):
    name = "ranking"
    start_urls = [
        'http://billboardtop100of.com/2015-2/',
    ]

    def parse(self, response):
        a = response.xpath("//h6/text()").getall()
        a[77] = a[77]+" "+a[78]
        a.remove("One")
        for i in range(100):    
            yield {
                'ranking': a[3*i],
                'artist': a[3*i+1],
                'song': a[3*i+2],
                'year': response.css('h1.entry-title::text').get()
            } 
