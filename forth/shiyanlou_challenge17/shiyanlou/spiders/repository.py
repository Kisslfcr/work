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
        for repository in response.css('li.public'):
            yield {
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
            }        
        
        
