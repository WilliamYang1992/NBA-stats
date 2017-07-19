# -*- coding: utf-8 -*-
import scrapy


class TeamGeneralTraditionalSpider(scrapy.Spider):
    name = 'team_general_traditional'
    allowed_domains = ['stats.nba.com']
    start_urls = ['http://stats.nba.com/teams/traditional']

    def parse(self, response):
        pass
