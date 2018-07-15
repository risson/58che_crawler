# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class Car58ChePipeline(object):
    def open_spider(self, spider):
        path = os.path.join(os.getcwd(), 'data', '{}.txt'.format(spider.name))
        self.fa = open(path, 'a+', encoding='utf-8')

    def close_spider(self, spider):
        self.fa.close()

    def process_item(self, item, spider):
        self.fa.write('{}\n'.format(str(item['info'])))
