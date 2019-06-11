#!/usr/bin/env python
# coding=utf-8
from pprint import pprint

import scrapy
from scrapy.selector import Selector
import logging

from woaidu.items import WoaiduItem

__auther__ = 'liazylee'
# connect='li233111@gmail.com'
# @Time    : 6/6/19 12:00 AM
# @FileName: woaidu.py
# @Software: PyCharm
# @project: woaidu

from scrapy import Spider


class WoaiduSpider(Spider):
    name = 'woaidu'
    start_urls = ['http://www.woaidu.org/sitemap_1.html',
                  'https://www.woaidu.org/xuanhuan_s1.html',
                  '']

    def parse(self, response):
        response_selector = Selector(response)
        next_page = response_selector.xpath('//div[@class="k2"]/div/a[text()="下一页"]/@href').extract_first()
        if next_page:
            url = 'http://www.woaidu.org' + next_page
            yield scrapy.Request(url=url, callback=self.parse)
        detail_links = response_selector.xpath('//div[contains(@class,"sousuolist")]/a/@href').extract()
        for detail_link in detail_links:
            url = 'http://www.woaidu.org' + detail_link
            # logging.log('{}'.format(url))
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_detail)

        pass

    def parse_detail(self, response):
        woaidu_item = WoaiduItem()
        # response_selector = Selector(response)
        response_selector = response.css('div.common-section-left.fl')

        #
        woaidu_item['book_name'] = response_selector.xpath('.//div[1]/div[1]/h1/text()').extract_first()
        woaidu_item['author'] = response_selector.xpath('.//div[1]/div[1]/p[2]/text()').extract_first().strip().replace(
            '作者：', '')
        woaidu_item['key_word'] = response_selector.xpath(
            './/div[1]/div[1]/p[4]/text()').extract_first().strip().replace('男主女主：', '')
        woaidu_item['data'] = response_selector.xpath('.//div[1]/div[1]/p[6]/text()').extract_first().strip().replace(
            ' 更新：', '')
        woaidu_item['book_covor_image'] = response_selector.xpath(
            './/div[1]/a[contains(@class,"Scover")]/img/@src').extract_first()
        response_selector = response.css(
            'body > div.content.widthWrap.detailWrap > div > div.common-section-left.fl > div:nth-child(5)')
        woaidu_item['book_description'] = response_selector.xpath(
            './/p[contains(@class,"listcolor descrition")]/text()').extract_first()
        response_selector = response.css(
            'body > div.content.widthWrap.detailWrap > div > div.common-section-left.fl > div:nth-child(9) > ul')
        download = []
        for x in response_selector.xpath('.//li'):
            download_item = {}

            download_item['url'] = x.xpath('.//a[2]/@href').extract_first()
            download_item['update_time'] = x.xpath('.//a[1]/text()').extract_first()
            download_item['source_site'] = x.xpath('.//a[1]/span/text()').extract_first()[3:-1]

            download.append(download_item)
        woaidu_item['book_dowload'] = str(download)
        pprint(woaidu_item)
        yield woaidu_item
