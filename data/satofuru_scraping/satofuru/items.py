# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class City(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()

class Gift(scrapy.Item):
    city = scrapy.Field()
    link = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
    price = scrapy.Field()
    star = scrapy.Field()
    review = scrapy.Field()
    img = scrapy.Field()