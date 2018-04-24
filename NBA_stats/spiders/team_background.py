# coding: utf-8

import re
import json

from scrapy import Spider
from scrapy import Request

from ..items import TeamBackground
from ..item_loaders import TeamBackgroundLoader


class TeamBackgroundSpider(Spider):
    """球队背景资料爬虫"""
    name = 'team_background'

    def start_requests(self):
        url = 'https://stats.nba.com/js/data/ptsd/stats_ptsd.js'
        yield Request(url=url)

    def parse(self, response):
        match = re.search('.*({.*}.)', response.text)
        if match:
            json_text = match.group(1)[:-2]
            data = json.loads(json_text)
            teams = data['teams']
            # 只有最后30支队伍才是NBA最新赛季的
            for team in teams[-30:]:
                team_id = team[0]
                name = team[3] + ' ' + team[4]
                tricode = team[1]
                loader = TeamBackgroundLoader(item=TeamBackground())
                loader.add_value('name', name)
                loader.add_value('tricode', tricode)
                url = 'https://stats.nba.com/stats/teamdetails?teamID={}'.format(team_id)
                meta = {'loader': loader}
                yield Request(url=url, callback=self.parse_background, meta=meta)

    def parse_background(self, response):
        meta = response.meta
        loader = meta['loader']
        data = json.loads(response.text)
        background = data['resultSets'][0]
        headers = background['headers']
        row_set = background['rowSet'][0]
        infos = {k: v for k, v in zip(headers, row_set)}
        loader.add_value('founded', infos['YEARFOUNDED'])
        loader.add_value('city', infos['CITY'])
        loader.add_value('arena', infos['ARENA'])
        loader.add_value('owner', infos['OWNER'])
        loader.add_value('general_manager', infos['GENERALMANAGER'])
        loader.add_value('head_coach', infos['HEADCOACH'])
        loader.add_value(
            'team_logo_url',
            'https://stats.nba.com/media/img/teams/logos/season/2017-18/{}_logo.svg'.format(
                loader.get_output_value('tricode'))
        )
        yield loader.load_item()
