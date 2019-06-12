# -*- coding: utf-8 -*-
import scrapy
import json
import re
from music.items import TaiheMusicTest
from scrapy_splash import SplashRequest


class TaiheSpider(scrapy.Spider):
    name = 'taihe'
    allowed_domains = ['y.taihe.com']

    def start_requests(self):
        start_urls = [
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=pop',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=rock',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=folk',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=electronic',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=gufeng',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=hiphop',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=metal',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=jazz',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=world',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=classical',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=esay',
            'http://y.taihe.com/data/musician/list?offset={offset}&num={num}&order=hot&genre=acg',

        ]
        for i in range(1, 6):
            for url in start_urls:
                url = url.format(offset=(i-1)*20, num=i*20)
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        texts = json.loads(response.text).get('artistList')
        for text in texts:
            item = TaiheMusicTest()
            artist_id = text.get('artist_id')
            item['fans_total'] = text.get('fans_total')
            item['hot'] = text.get('hot')
            item['url'] = 'http://y.taihe.com/artist/' + artist_id
            item['name'] = text.get('name')
            item['genre'] = text.get('genre')
            item['avatar'] = text.get('avatar')
            item['artist_id'] = artist_id
            yield SplashRequest(url=item['url'], callback=self.parse_tags, dont_filter=True, meta={'item': item}, args={'wait': 0.5}, encoding='utf8')

    def parse_tags(self, response):
        item = response.meta.get('item')
        tags = response.xpath("//div[@class='info']/p[@class='style clearfix'][2]/span[@class='more']/text()").extract_first().split(',')
        item['tags'] = tags
        yield item