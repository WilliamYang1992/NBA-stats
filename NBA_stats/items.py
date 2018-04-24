# coding: utf-8

from scrapy import Item, Field


class TeamBackground(Item):
    name = Field()
    tricode = Field()
    founded = Field()
    city = Field()
    arena = Field()
    owner = Field()
    general_manager = Field()
    head_coach = Field()
    team_logo_url = Field()
