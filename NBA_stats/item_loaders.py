# coding: utf-8

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class TeamBackgroundLoader(ItemLoader):
    default_input_processor = MapCompose(lambda x: str.strip(x) if isinstance(x, str) else x)
    default_output_processor = TakeFirst()
