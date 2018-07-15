from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings
from car58che.spiders.carlist import CarSpider
from car58che.spiders.comment import CommentSpider

process = CrawlerProcess(settings)

def getSpider(crawlerClass):
    if isinstance(crawlerClass,Spider):
        return crawlerClass
    else:
        return crawlerClass()

# 加载单个爬虫
def proc(crawlerClass):
    process.crawl(getSpider(crawlerClass))

# 单独跑几个爬虫
def run(crawlerClassList):
    processNum = 0
    for each in crawlerClassList:
        if(hasattr(each, 'main')):
            spider = getSpider(each)
            spider.main()
        else:
            processNum += 1
            proc(each)

    if (processNum > 0):
        process.start()

if __name__ == '__main__':
    run([CommentSpider])