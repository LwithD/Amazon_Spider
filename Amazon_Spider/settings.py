# Scrapy settings for Amazon_Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

#proxy
import json
import requests

BOT_NAME = 'Amazon_Spider'

SPIDER_MODULES = ['Amazon_Spider.spiders']
NEWSPIDER_MODULE = 'Amazon_Spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Amazon_Spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Connection': 'keep-alive',
  'Accept-Encoding':'gzip, deflate, br',
  'cookie':'"session-id=132-7361795-9934902; i18n-prefs=USD; ubid-main=132-8733755-6723145; session-id-time=2082787201l; _msuuid_jniwozxj70=9D0163B8-1DB6-40C1-B79A-2E7FE6BF635B; s_vnum=2052036977725%26vn%3D2; s_nr=1620093912897-Repeat; s_dslv=1620093912899; s_fid=010F1C5CADB81738-2C7FB0627453304C; regStatus=pre-register; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1620543230141-504697.38_0; lc-main=en_US; session-token=JCVKGJEgiMCJcKNNPk5ilkROqjxOa/9SHZk5UOo7QcIo4cf3BsiC678gVjgu7hIAP1AFw6xPV9OhtEzMr+gy4e49Sjm6WhRTy14Sv672FiXDNgCVxISJdj5XDSd0Oh6p/ZEMhvb39JlIJRu86UQNKevvpIeof+7uBjKVyy11MhFV4xNXFRefe/ewfNXHgVP0; csm-hit=adb:adblk_no&t:1620634526954&tb:9FMG25R5H8GGFAXSZQZX+b-9FMG25R5H8GGFAXSZQZX|1620634526954"',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Amazon_Spider.middlewares.AmazonSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Amazon_Spider.middlewares.AmazonSpiderDownloaderMiddleware': 500,
   'Amazon_Spider.middlewares.ProxyMiddleWare':543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Amazon_Spider.pipelines.AmazonSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True  #限速
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


PROXY_POOL = ['']

# print('1')

def refresh_pool():
    url = ''
    json = requests.get(url).json()
    global PROXY_POOL
    pool = []
    for i in json['data']:
        proxy = 'https://'+str(i['ip'])+':'+str(i['port'])
        pool.append(proxy)
    print(pool)
    PROXY_POOL = pool