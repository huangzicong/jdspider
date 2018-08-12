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
        start_url = ['https://search.jd.com/Search?keyword=名著&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=' + str(i) for i in
                  range(1, 200, 2)]
        for url in start_url:
            yield Request(url=url,callback=self.parse,dont_filter=True)
    def parse(self, response):
        name = response.xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em')
        bookname = name.xpath('string(.)').extract()[0]
        print(bookname)
        for i in range(1,61):
            try:

                name = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/div/div[3]/a/em')
                bookname = name.xpath('string(.)').extract()[0]
                id = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/@data-sku').extract()[0]
                ratenum = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/div/div[5]/strong')
                num = ratenum.xpath('string(.)').extract()[0]
                bookprice = response.xpath('//*[@id="J_goodsList"]/ul/li['+str(i)+']/div/div[2]/strong/i')
                price = bookprice.xpath('string(.)').extract()[0]
                bookitem = JdbookItem()
                bookitem['name'] = bookname
                bookitem['id'] = id
                bookitem['num'] = num
                bookitem['price'] = price
                yield bookitem

            except Exception:
                continue

