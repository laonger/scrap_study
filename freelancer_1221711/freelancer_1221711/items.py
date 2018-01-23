# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


names = {
    des           : 'Description',
    addr          : 'Address',
    link          : 'Link',
    image         : 'Main_Image',
    price         : 'Valor',
    area          : 'Superficie',
    bath_bed      : 'BathBed',
    coordinate    : 'Coordinates',
    subway_1_time : 'Wallking Distance Subway1 (Minutes)',
    subway_2_time : 'Wallking Distance Subway2 (Minutes)',
    subway_3_time : 'Wallking Distance Subway3 (Minutes)',
    subway_1_name : 'NAME Subway1 (Minutes)',
    subway_2_name : 'NAME Subway2 (Minutes)',
    subway_3_name : 'NAME Subway3 (Minutes)',
}


class Freelancer1221711Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    des           : scrapy.Field(),
    addr          : scrapy.Field(),
    link          : scrapy.Field(),
    image         : scrapy.Field(),
    price         : scrapy.Field(),
    area          : scrapy.Field(),
    bath_bed      : scrapy.Field(),
    coordinate    : scrapy.Field(),
    subway_1_time : scrapy.Field(),
    subway_2_time : scrapy.Field(),
    subway_3_time : scrapy.Field(),
    subway_1_name : scrapy.Field(),
    subway_2_name : scrapy.Field(),
    subway_3_name : scrapy.Field(),

