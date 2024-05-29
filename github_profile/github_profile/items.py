# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubProfileItem(scrapy.Item):
    username = scrapy.Field()
    name = scrapy.Field()
    bio = scrapy.Field()
    social_accounts = scrapy.Field()
    number_of_repositories = scrapy.Field()
    number_of_stars = scrapy.Field()
