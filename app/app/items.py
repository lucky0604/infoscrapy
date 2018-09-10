# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # created_time = scrapy.Field()
    product_name = scrapy.Field()
    num = scrapy.Field()
    location = scrapy.Field()
    destination = scrapy.Field()
    contact_user = scrapy.Field()
    contact_phone = scrapy.Field()
    product_type = scrapy.Field()
    msg_type = scrapy.Field()
