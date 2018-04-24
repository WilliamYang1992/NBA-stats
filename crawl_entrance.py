# -*- coding: utf-8 -*-

"""
Scrapy 运行入口

"""

import sys

from scrapy.cmdline import execute

spider_name = sys.argv[1]
execute('scrapy crawl {}'.format(spider_name).split())
