# -*- coding: utf-8 -*-

import scrapy


class RankingSpider(scrapy.Spider):
    name = "ranking"
    start_urls = [
        'http://billboardtop100of.com/2016-2/',
    ]

    def parse(self, response):
        sas = response.xpath('//table[@class="sortable alternate songtable"]/tbody/tr/td/text()')
        for i in range(100):    
            yield {
                'ranking': sas[3*i].get(),
                'artist': sas[3*i+1].get(),
                'song': sas[3*i+2].get().replace("\n", ""),
                'year': response.css('h1.entry-title::text').get()
            } 