# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    rating = scrapy.Field()
    rating_num = scrapy.Field()
    price_kindle = scrapy.Field()
    price_hard = scrapy.Field()
    price_paper = scrapy.Field()
    price_audioCD = scrapy.Field()
