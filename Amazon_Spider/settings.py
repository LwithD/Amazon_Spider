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
COOKIES_ENABLED = True


COOKIES_DEBUG = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Connection': 'keep-alive',
  'Accept-Encoding':'gzip, deflate, br',
  'cookie':'session-id=132-7361795-9934902; i18n-prefs=USD; ubid-main=132-8733755-6723145; session-id-time=2082787201l; _msuuid_jniwozxj70=9D0163B8-1DB6-40C1-B79A-2E7FE6BF635B; s_vnum=2052036977725%26vn%3D2; s_nr=1620093912897-Repeat; s_dslv=1620093912899; s_fid=010F1C5CADB81738-2C7FB0627453304C; regStatus=pre-register; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1620543230141-504697.38_0; lc-main=en_US; sp-cdn="L5Z9:CN"; session-token=xq3dpAmV2k2MvfACZ11fWZ97vIILtSaPIHTeFegSnCHd7dHQkRa348V6RgcZAtC1w6OFW4ZV/MnG0iGhfIKLyIl2GMjmQzXJI+hgg67mGC57io48gGB86lZUMhHF1s0NAZLUoTQy+gYHLaIOlOHIEbjDS0z+wqCN8pn24KWcRegYnAlUtQnWmLu0xxVp7MFu; skin=noskin; csm-hit=s-QJCZMY8XEVE6803PY0TP|1620809077128',
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
   # 'Amazon_Spider.middlewares.ProxyMiddleWare':543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Amazon_Spider.pipelines.AmazonSpiderPipeline': 300,
   'Amazon_Spider.pipelines.AmazonMysqlPipeline':300,
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

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy-redis组建自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#配置调度器是否持久化（即爬虫结束后是否清空请求队列和set缓存
SCHEDULER_PERSIST = True

REDIS_HOST = '127.0.0.1' #远程IP
REDIS_PORT = 6379

PROXY_POOL = [
   '8.133.191.41:8081',
   '223.215.18.173:9999',
   '59.33.55.238:9999',
   '58.253.155.104:9999',
   '175.146.210.38:9999',
   '49.70.48.147:9999',
   '58.253.156.188:9999',
   '223.240.208.97:8888',
   '58.253.157.162:9999',
   '49.86.178.46:9999',
   '49.70.99.118:9999',
   '49.89.143.61:9999',
   '223.243.245.29:9999',
   '58.253.153.52:9999',
   '59.33.56.229:9999',
   '27.43.188.23:9999',
   '49.70.99.102:9999',
   '220.249.149.69:9999',
   '60.168.80.4:1133',
   '42.238.85.90:9999',
   '58.253.157.5:9999',
   '36.250.156.3:9999',
   '58.255.206.129:9999',
   '223.241.119.66:8888',
   '58.253.157.214:9999',
   '49.89.143.68:9999',
   '58.253.152.62:9999',
   '58.253.158.212:9999',
   '49.70.48.31:9999',
   '60.168.206.132:1133',
   '58.253.152.173:9999',
   '58.253.155.119:9999',
   '49.89.85.127:9999',
   '49.70.85.142:9999',
   '58.253.157.35:9999',
   '49.70.95.1:9999',
   '60.19.236.172:9999',
   '58.22.177.66:9999',
   '58.253.152.191:9999',
   '60.168.207.62:8888',
   '49.89.84.207:9999',
   '58.253.155.73:9999',
   '58.253.158.105:9999',
   '49.70.32.51:9999',
   '49.89.87.204:9999',
   '60.168.80.27:8888',
   '49.70.32.149:9999',
   '58.253.155.15:9999',
   '58.253.153.78:9999',
   '58.255.199.252:9999',
   '58.253.157.189:9999',
   '223.243.244.52:9999',
   '182.46.98.229:9999',
   '60.168.206.45:1133',
   '42.238.70.150:9999',
   '58.253.157.206:9999',
   '58.253.152.20:9999',
   '113.195.171.47:9999',
   '60.168.206.207:1133',
   '49.70.64.21:9999',
   '60.168.81.191:1133',
   '49.70.85.68:9999',
   '171.35.147.37:9999',
   '104.129.194.34:8800',
   '104.129.196.120:8800',
   '104.129.196.181:8800',
   '175.43.35.15:9999',
   '58.253.152.238:9999',
   '58.253.153.135:9999',
   '60.167.159.234:9999',
   '58.253.155.253:9999',
   '121.226.214.62:9999',
   '120.83.106.95:9999',
   '58.253.154.146:9999',
   '223.247.164.196:9999',
   '182.46.97.193:9999',
   '42.238.70.182:9999',
   '58.253.154.213:9999',
   '115.53.34.247:9999',
   '58.253.158.215:9999',
   '120.83.104.156:9999',
   '49.86.183.54:9999',
   '220.179.214.10:8888',
   '123.169.114.66:9999',
   '36.248.132.186:9999',
   '59.33.52.96:9999',
   '60.167.133.56:8888',
   '123.169.116.6:9999',
   '59.33.52.178:9999',
   '175.43.34.11:9999',
   '175.146.215.182:9999',
   '60.168.207.95:1133',
   '120.83.107.99:9999',
   '182.46.121.58:9999',
   '59.33.97.138:9999',
   '182.46.111.10:9999',
   '49.86.177.111:9999',
   '223.247.168.64:9999',
   '223.215.10.58:9999',
   '223.247.170.231:9999',
]

# print('1')

def refresh_pool():
   #  url = ''
   #  json = requests.get(url).json()
   #  global PROXY_POOL
   #  pool = []
   #  for i in json['data']:
   #      proxy = 'https://'+str(i['ip'])+':'+str(i['port'])
   #      pool.append(proxy)
   #  print(pool)
   #  PROXY_POOL = pool
   pass