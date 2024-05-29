import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Response
from accuweather.items import AccuweatherItem


class WeatherSpider(CrawlSpider):
    name = "weather"
    allowed_domains = ["www.accuweather.com"]
    start_urls = ["https://www.accuweather.com/fa/ir/iran-weather"]
    
    rules = (Rule(LinkExtractor(allow=r"web-api/"), callback="city", follow=True),)
    
    def city(self, response: Response):
        items = AccuweatherItem() 
        items['city'] = response.xpath('/html/body/div/div[1]/div[1]/div/a[2]/h1/text()').get()
        items['weather_temperature'] = response.xpath('/html/body/div/div[5]/div[1]/div[1]/a[1]/div[2]/div[1]/div[1]/div/div[1]/text()').get()
        items['time'] = response.xpath('/html/body/div/div[7]/div[1]/div[1]/a[1]/div[1]/p/text()').get()
        items['wind_speed'] = response.xpath('/html/body/div/div[5]/div[1]/div[1]/a[1]/div[2]/div[2]/div[1]/span[2]/text()').get()
        items['high_wind_speed'] = response.xpath('/html/body/div/div[5]/div[1]/div[1]/a[1]/div[2]/div[2]/div[2]/span[2]/text()').get()
        items['air_quality'] = response.xpath('/html/body/div/div[5]/div[1]/div[1]/a[1]/div[2]/div[2]/div[3]/span[2]/text()').get()
        return items