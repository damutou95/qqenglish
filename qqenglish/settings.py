# -*- coding: utf-8 -*-



BOT_NAME = 'qqenglish'

SPIDER_MODULES = ['qqenglish.spiders']
NEWSPIDER_MODULE = 'qqenglish.spiders'



ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32



#DOWNLOAD_DELAY = 3

#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


DOWNLOADER_MIDDLEWARES = {

    'qqenglish.middlewares.ProxyMiddleware': 543,
    'qqenglish.middlewares.QqenglishDownloaderMiddleware': 800,
}




