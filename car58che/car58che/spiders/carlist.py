# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from car58che.items import Car58CheItem
from car58che.settings import CAR_MAPS
import numpy as np
import re


class CarSpider(scrapy.Spider):
    name = 'carlist'
    allowed_domains = ['www.58che.com']
    start_urls = []

    def start_requests(self):
        prefix = [list(np.repeat(x,y)) for x, y in CAR_MAPS.items()]
        pagenum = [list(range(i)) for _, i in CAR_MAPS.items()]
        prefix = list(np.hstack(prefix))
        pagenum = list(np.hstack(pagenum))
        urls = [x+'_n'+str(y+1)+'.html' for x, y in zip(prefix, pagenum)]

        for url in urls:
            yield Request(url)

    def parse(self, response):
        item = Car58CheItem()
        ids = self.parse_info(response.text, 'www.58che.com/?(\\d+)/', 1)
        for i in ids:
            item['info'] = i.strip()
            yield item

    def parse_info(self, r, p, i=1):
        try:
            pattern = re.compile(p, re.S)

            items = re.findall(pattern, r)
            if not i:
                item = items[i]
            else:
                item = items
        except Exception as e:
            print('parse_info:' + str(e))
            item = ''
        finally:
            return item