# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class WoaiduItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mongo_id=Field()
    book_name=Field()
    author=Field()
    book_description=Field()
    book_covor_image=Field()
    book_dowload=Field()
    book_file_url=Field()
    book_file=Field()
    key_word=Field()
    data=Field()

    pass
