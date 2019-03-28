# -*- coding: utf-8 -*-
import scrapy
from taoche.items import TaocheItem


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['taoche.com']
    start_urls = []
    with open('D:/爬虫/taoche/taoche/城市和车型.txt', 'r') as f:
        all_sj = f.readlines()
    city_list = eval(all_sj[0].strip('\n'))
    car_list = eval(all_sj[-1].strip('\n'))
    for city in city_list:
        for car in car_list:
            url = 'https://{}.taoche.com/{}/'.format(city, car)
            start_urls.append(url)
    def parse(self, response):
        all_page = response.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()').extract()
        if all_page:
            big_page = int(all_page[0])
        else:
            big_page = 1
        for i in range(1, big_page+1):
            url = response.url + '?page={}'.format(str(i))
            yield scrapy.Request(url=url, callback=self.parse1)


    def parse1(self, response):
        li_list = response.xpath('//div[@id="container_base"]/ul[@class="gongge_ul"]/li')
        for li in li_list:
            item = TaocheItem()
            name = li.xpath('./div[@class="gongge_main"]/a/span/text()').extract()[0]
            item['name'] = name
            spsj = li.xpath('./div[@class="gongge_main"]/p/i[1]/text()').extract()[0]
            item['spsj'] = spsj
            gls = li.xpath('./div[@class="gongge_main"]/p/i[2]/text()').extract()[0]
            item['gls'] = gls
            address = li.xpath('./div[@class="gongge_main"]/p/i[@class="city_i"]/a/text()').extract()[0]
            item['address'] = address
            money = li.xpath('./div[@class="gongge_main"]/div[@class="price"]/i[@class="Total brand_col"]/text()').extract()[0]
            item['money'] = money
            data_url = li.xpath('./div[@class="gongge_main"]/a/@href').extract()[0]
            yield scrapy.Request(url="https:"+data_url, callback=self.parsel2, meta={'data':item}, dont_filter=False)


    def parsel2(self, response):
        item = response.meta['data']
        pl = response.xpath('//div[@class="detail-summary"]/div[@class="summary-attrs"]/dl[3]/dd/text()').extract()[0]
        item['pl'] = pl
        yield item
