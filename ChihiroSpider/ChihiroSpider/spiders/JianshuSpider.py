# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from ..items import JianshuItem, JianshuItemLoader
import re
from typing import Generator, Any
from scrapy_redis.spiders import RedisSpider


class JianshuSpider(RedisSpider):
    name = 'JianshuSpider'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['https://www.jianshu.com/c/V2CqjW?order_by=added_at']
    base_url = 'https://www.jianshu.com'
    page_num = 1
    crawled = 0

    custom_settings = {
        "JOBDIR": "spider_info/jianshu",
    }

    def parse(self, response) ->Generator[Request, Any, None]:
        top_tags = response.xpath("//div[@class='main-top']/div[@class='info']/text()").extract()[0]
        total_nums = int(re.findall(r'\d+', top_tags)[0])
        article_urls = response.xpath("//ul[@class='note-list']/li/a/@href").extract()
        for url in article_urls:
            yield Request(url=parse.urljoin(self.base_url, url), callback=self.parse_detail)
            self.crawled += 1
        if self.crawled < total_nums:
            self.page_num += 1
            next_page_url = self.start_urls[0] + "&page={0}" .format(self.page_num)
            yield Request(url=next_page_url, callback=self.parse)

    def parse_detail(self, response) -> Generator[scrapy.Item, Any, None]:
        item_loader = JianshuItemLoader(item=JianshuItem(), response=response)
        item_loader.add_value("url", response.url)
        item_loader.add_xpath("title", "//div[@class='article']/h1/text()")
        item_loader.add_xpath('content', "//div[@class='show-content-free']")

        jianshu_item = item_loader.load_item()

        yield jianshu_item