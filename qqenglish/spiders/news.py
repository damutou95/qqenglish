# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urljoin
import re

class NewsSpider(scrapy.Spider):
    name = 'news'
    #allowed_domains = ['sss']
    start_urls = ['http://www.qqenglish.com/bn/bn/', 'http://www.qqenglish.com/bn/business/', 'http://www.qqenglish.com/bn/technology/', 'http://www.qqenglish.com/bn/education/', 'http://www.qqenglish.com/bn/culture/', 'http://www.qqenglish.com/bn/style/', 'http://www.qqenglish.com/bn/health/', 'http://www.qqenglish.com/bn/science/', 'http://www.qqenglish.com/bn/travel/', 'http://www.qqenglish.com/bn/opinion/']
    headers= {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    def start_requests(self):
        for i in self.start_urls:
            yield Request(i, headers=self.headers, callback=self.parse, meta={'tag': 0})

    def parse(self, response):
        pageNum = int(re.findall('List_(\d+).htm', response.xpath('//a[contains(text(),"下一页")]/@href').extract_first())[0])
        urls = [response.url + f'List_{x+1}.htm' for x in range(pageNum)]
        urls.append(response.url)
        for url in urls:
            yield Request(url, callback=self.parsePlus, headers=self.headers, meta={'tag': 0})

    def parsePlus(self, response):
        reList = response.xpath('//div[@id="list"]//ul/li/a/@href').extract()
        list = [urljoin(response.url, x) for x in reList]
        for url in list:
            with open('saved.txt', 'r') as f:
                i = f.readlines()
                saved = [x.strip('\n') for x in i]
                #如果网址已经爬过那就去重
                if url not in saved:
                    yield Request(url, callback=self.parseItem, headers=self.headers, meta={'tag': 0, 'saved': True})
    #详情页
    def parseItem(self, response):
        print('进入网页' + response.url)
        title = response.xpath('//div[@id="leftN_title"]/h2/text()').extract_first().replace('/', '')
        fileName = ''.join(response.url.split('/')[-2:])
        content = response.xpath('//div[@class="content"]/p[not(@align)]')
        sentences = [i.xpath('string(.)').extract_first() for i in content]
        s = '\n'.join(sentences[2:])
        if '（英文）' not in title:
            with open(title + fileName.strip('.') + '.txt', 'w') as f:
                #发现结果第一行出来是中英文在一行的做简单处理
                f.write(s)




