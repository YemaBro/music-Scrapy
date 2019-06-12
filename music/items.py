# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QQMusic(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # collection = table = 'singer'
    # 歌曲id
    id = scrapy.Field()
    # 歌手名字
    singer_name = scrapy.Field()
    # 歌名
    song_name = scrapy.Field()
    # 歌曲地址
    song_url = scrapy.Field()
    # 歌词
    lrc = scrapy.Field()
    # 评论
    comment = scrapy.Field()


class TaiheMusicTest(scrapy.Item):
    fans_total = scrapy.Field()
    hot = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    genre = scrapy.Field()
    avatar = scrapy.Field()
    artist_id = scrapy.Field()


