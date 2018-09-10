# -*- coding: utf-8 -*-
import scrapy
from app.items import AppItem
import re


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['http://www.cn156.com/']
    start_urls = ['http://www.cn156.com/news/lianyun/']

    def parse(self, response):
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
        item = AppItem()

