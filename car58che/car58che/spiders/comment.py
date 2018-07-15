# -*- coding: utf-8 -*-
import os
import demjson
import scrapy
from scrapy.http import Request
from car58che.items import Car58CheItem
from car58che.settings import CM_URL, CM_TYPES


class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = []
    start_urls = ['http://www.58che.com']

    def parse(self, response):
        path = os.path.join(os.getcwd(), 'data', 'carlist.txt')
        fr = open(path, 'r')
        urls = [(CM_URL.format(i.strip(), s, j), j, s) for i in fr.readlines() for j in range(20) for _, s in CM_TYPES.items()]
        fr.close()
        for url, page, score in urls:
            yield Request(url, meta={'page': page, 'score': score}, callback=self.parse_comment)

    def parse_comment(self, response):
        item = Car58CheItem()
        meta = response.meta
        comments = response.xpath('//div[@class="pingyu"]/text()').extract()
        if comments is None: 
            return False
        for comment in comments:
            item['info'] = '{} {}'.format(meta['score'], comment.strip())
            yield item
        return True

        
        

