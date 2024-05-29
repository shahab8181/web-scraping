# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def get_city(value: str):
    return value.split(',')[1]

class AccuweatherItem(scrapy.Item):
    city = scrapy.Field()
    weather_temperature = scrapy.Field()
    time = scrapy.Field()
    wind_speed = scrapy.Field()
    high_wind_speed = scrapy.Field()
    air_quality = scrapy.Field()
