#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'Lucky'

import scrapy
from app.items import AppItem
import re

class InfoScrapy(scrapy.spiders.Spider):
    name = 'info'
    start_urls = [
        'http://peihuo.haoyun56.com/goods_a830000.html'
    ]

    def parse(self, res):
        current_url = res.url
        body = res.body
        unicode_body = res.body_as_unicode()
        item = AppItem()

        item['product_name'] = res.xpath('//tr/td/a/text()').extract()
        item['num'] = res.xpath('//tr/td[4]/text()').extract()
        item['location'] = res.xpath('//tr/td[2]/text()').extract()
        item['destination'] = res.xpath('//tr/td[3]/text()').extract()
        pArr = []
        nArr = []
        lArr = []
        dArr = []

        for i in item['product_name'][13:]:
            i = i.strip()
            if i != '详细':
                pArr.append(i)

        for j in item['num'][7:]:
            j = j.strip()
            nArr.append(j)
        for m in item['location'][16:]:
            m = m.strip()
            lArr.append(m)

        for n in item['destination'][7:]:
            n = n.strip()
            dArr.append(n)
        for k in pArr:
            item['product_name'] = k
        item['product_name'] = pArr
        item['num'] = nArr
        item['location'] = lArr
        item['destination'] = dArr
        yield item
