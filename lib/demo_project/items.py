# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


class techItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tech_news=scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor= TakeFirst()
    )

class footballItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    football_news=scrapy.Field(
        input_processor= MapCompose(remove_tags),
       output_processor= TakeFirst()
    )
class cricketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cricket_news=scrapy.Field(
        input_processor= MapCompose(remove_tags),
       output_processor= TakeFirst()
    )

class newsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    top_news=scrapy.Field(
        input_processor= MapCompose(remove_tags),
       output_processor= TakeFirst()
    )
      
