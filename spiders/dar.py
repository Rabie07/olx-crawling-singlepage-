# -*- coding: utf-8 -*-
import scrapy
from ..items import DarazzItem
import csv

class DarSpider(scrapy.Spider):
    name = 'dar'
    start_urls = ['https://www.olx.com.pk/items/q-samsung-galaxy-note']

    def parse(self, response):
        items = DarazzItem()

        # image_link = ('.cRjKsc .c1ZEkM::attr(src)').extract()
        # product_name = response.css('.c16H9d a::text').extract()
        product_price = response.css('._89yzn::text').extract()

        # items['image link'] = image_link
        # items['product_name'] = product_name
        items['product_price'] = product_price

        with open('%s_tweets.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["price"])
            writer.writerow(product_price)

        yield items


