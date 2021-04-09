# encoding=utf-8
from scrapy import Item,Field

class SogouItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = Field()
    title = Field()
    abstract = Field()
    pubTime = Field()
    source = Field()
    url = Field()
    topic = Field()