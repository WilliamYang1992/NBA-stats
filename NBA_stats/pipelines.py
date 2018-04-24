# -*- coding: utf-8 -*-

import requests


class TeamBackgroundPipeline:

    def process_item(self, item, spider):
        if spider.name == 'team_background':
            data = {
                'name': item.get('name'),
                'founded': item.get('founded'),
                'city': item.get('city'),
                'arena': item.get('arena'),
                'owner': item.get('owner', ''),
                'general_manager': item.get('general_manager', ''),
                'head_coach': item.get('head_coach', ''),
                'team_logo_url': item.get('team_logo_url', '')
            }
            url = 'http://127.0.0.1:8000/stats/teams/create/'
            try:
                r = requests.post(url, data=data)
            except requests.RequestException as e:
                print(e)
            else:
                print(item.get('name'))
                print(r.text)
        return item
