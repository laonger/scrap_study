#!/usr/bin/python
# encoding: utf-8

import time
import copy
import scrapy


class A(scrapy.Spider):
    """# A: docstring"""
    name = "a"
    allowed_domains = [
        "portalinmobiliario.com",
    ]
    start_urls = [
        "https://www.portalinmobiliario.com/venta/departamento/centro-historico-de-santiago-santiago-santiago-metropolitana?tp=2&;op=1&ca=3&ts=1&dd=2&dh=4&bd=1&bh=3&or=&mn=2&sf=1&sp=1&pd=2.500&sd=60,00&sh=100,00",
    ]
    link_head = 'https://www.portalinmobiliario.com'
    one_record = {
        'des': '',
        'link': '',
        'image': '',
        'price': '',
        'area': '',

        'DB': '',
        'addr': '',
    }

    # 3754873

    def parse(self, response):
        """# parse: docstring """
        items = response.css('div.products-list')
        items = items.css('div.row.product-item')      
        l = []
        f = open('link', 'w+')
        for i, item in enumerate(items):
            this_record = copy.deepcopy(self.one_record)
            image_block = item.css('div.col-sm-3')
            image = image_block.xpath('a/img/@src').extract_first()
            this_record['image'] = image

            info_block = item.xpath('div[@class="col-sm-9 product-item-data"]/div[@class="row"]')
            some_info = info_block.css('div.col-sm-6')

            product_type_1 = some_info.xpath('p[1]/span[@class="product-type-title"]/text()').extract_first()
            product_type_2 = some_info.xpath('p[1]/text()').extract_first()
            this_record['des'] = product_type_1+product_type_2

            link = some_info.xpath('h4/a/@href').extract_first()
            this_record['link'] = self.link_head+link
            f.write(this_record['link'])
            f.write('\n')

            price_area = info_block.xpath('div[@class="col-sm-3"]/p[@class="product-property"]/span/text()').extract()
            if len(price_area) > 2:
                price = ' - '.join(price_area[:2])
            else:
                price = price_area[0]
            area = price_area[-1]
            this_record['price'] = price
            this_record['area'] = area

            #if product_type_1 == 'Proyecto, ':
            #    request = scrapy.Request(this_record['link'], self.parse_page_1)
            #    request.meta['data_'] = this_record
            #    time.sleep(1)
            #    yield request
            #elif product_type_1 == 'Propiedad usada, ':
            #    print 2
            #else:
            #    raise
        f.close()
            


    def parse_page_1(self, response):
        """# parse_page: docstring """
        this_record = response.meta['data_']
        DB_block = response.xpath('//div[@id="wrapper"]/section[@class="project-features-section"]/div/div[@class="row prj-infographics hi-density"]/div[@class="project-feature-item"]')
        if DB_block:
            d = DB_block[1].xpath('span[@class="project-feature-details"]/em/text()')
            d = d.extract_first().replace(' ', '').replace('a', ',')+'D'
            b = DB_block[2].xpath('span[@class="project-feature-details"]/em/text()')
            b = b.extract_first().replace(' ', '').replace('a', ',')+'B'
            DB = d+'/'+b
            this_record['DB'] = DB

            addr = ', '.join(response.xpath('//p[@class="prj-map-addr-obj"]/span/text()').extract())
            this_record['addr'] = addr
        yield this_record
            





        

