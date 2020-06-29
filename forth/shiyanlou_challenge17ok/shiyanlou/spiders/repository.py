# -*- coding: utf-8 -*-
import scrapy
from ..items import RepositoryItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        url_list = ['https://github.com/shiyanlou?tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODozMzozNyswODowMM4FkpMh&tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wNlQxMzoxNToyMiswODowMM4FkjnP&tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0xNlQxMDo0MTowMiswODowMM4BrEWs&tab=repositories',
                    'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0wM1QwODo1OToxMSswODowMM4BjgTX&tab=repositories']
        return url_list

    def parse(self, response):
        for course in response.css('li.public'):
            print('++++++',course)
            item = RepositoryItem(
                name =  course.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                update_time = course.xpath('.//relative-time/@datetime').extract_first()
            )        
            print('&&&&&&&',item)
            course_url = course.xpath('.//a/@href').extract_first()
            print('------',course_url)
            full_course_url = response.urljoin(course_url)
            request = scrapy.Request(full_course_url, self.parse_author)
            request.meta['item'] = item
            print('******',request)
            yield request
        
        
    def parse_author(self, response):
        item = response.meta['item']
        print(response)
        item['commits'] = response.xpath('//ul[@class="numbers-summary"]//span[1]/text()').extract()[0].strip()
        item['branches'] = response.xpath('//ul[@class="numbers-summary"]//span[1]/text()').extract()[1].strip()
        item['releases'] = response.xpath('//ul[@class="numbers-summary"]//span[1]/text()').extract()[3].strip()
        yield item
