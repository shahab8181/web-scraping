from scrapy import Spider, Request
from scrapy.http import Response
from scrapy.crawler import CrawlerProcess
from scrapy_splash import  SplashRequest


class TgjuSpider(Spider):
    name = 'tgju'
    
    def start_requests(self):
        yield Request(url=r'https://www.tgju.org/', callback=self.parse)
        
    def parse(self, response: Response):
        for div in response.css('div.fs-row'):
            for subdiv in response.css('div.fs-cell.fs-sm-12.fs-xs-12.fs-md-12.fs-lg-12.fs-xl-6.table-tag-row'):
                table = subdiv.css('table tbody')
                for tr in table:
                    yield {
                        'نام': tr.css('th::text').get(),
                        'قیمت زنده': tr.css('td::text').getall()[0],
                        'کمترین': tr.css('td::text').getall()[1],
                        'زمان': tr.css('td::text').getall()[3],
                    }
                

spider_conf = CrawlerProcess(settings={
    'FEEDS': {
        r'C:\Users\shahab\Desktop\tgju_result.csv': {'format': 'csv', 'encoding': 'utf8'},
        r'C:\Users\shahab\Desktop\tgju_result.json': {'format': 'json', 'encoding': 'utf8'},
        r'C:\Users\shahab\Desktop\tgju_result.jl': {'format': 'jl', 'encoding': 'utf8'}
    }
})

spider_conf.crawl(TgjuSpider)
spider_conf.start()