# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy import Request
from ..items import JdbookItem
class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['search.jd.com']
    start_urls = ['http://search.jd.com/']
    def start_requests(self):
        start_url = ['https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page='+str(i) for i in range(1,199,2)]
        for url in start_url:
            yield Request(url=url,callback=self.parse,dont_filter=True)
    def parse(self, response):
        for i in range(1,61):
            try:

                name = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/div/div[3]/a/em')
                bookname = name.xpath('string(.)').extract()
                id = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/@data-sku').extract()
                ratenum = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/div/div[4]/strong')
                num = ratenum.xpath('string(.)').extract()
                bookprice = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/div/div[2]/strong/i')
                price = bookprice.xpath('string(.)').extract()
                bookitem = JdbookItem()
                bookitem['name'] = bookname
                bookitem['id'] = id
                bookitem['num'] = num
                bookitem['price'] = price
                yield bookitem

            except Exception:
                continue

